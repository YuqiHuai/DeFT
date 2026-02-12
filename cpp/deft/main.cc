/**
 * @file main.cc
 * @author Yuqi Huai <yhuai@uci.edu>
 *
 * @brief Loads and executes planning module tests extracted by DeFT.
 *
 * This program initializes the planning test framework, loads test cases
 * produced by DeFT, and executes them for offline validation and regression
 * testing.
 *
 * Usage:
 *   /apollo/bazel-bin/modules/deft/main
 */


#include <chrono>
#include <iostream>
#include <map>
#include <string>
#include <cstdlib>

#include "cyber/proto/record.pb.h"
#include "modules/canbus/proto/chassis.pb.h"
#include "modules/common/proto/pnc_point.pb.h"
#include "modules/localization/proto/localization.pb.h"
#include "modules/perception/proto/traffic_light_detection.pb.h"
#include "modules/planning/proto/planning.pb.h"
#include "modules/planning/proto/planning_internal.pb.h"
#include "modules/prediction/proto/prediction_obstacle.pb.h"
#include "modules/routing/proto/routing.pb.h"
#include "modules/storytelling/proto/story.pb.h"

#include "cyber/cyber.h"
#include "cyber/init.h"
#include "cyber/message/raw_message.h"
#include "cyber/record/record_message.h"
#include "cyber/record/record_reader.h"
#include "cyber/record/record_writer.h"
#include "cyber/time/clock.h"
#include "modules/map/hdmap/hdmap_util.h"
#include "modules/planning/common/dependency_injector.h"
#include "modules/planning/on_lane_planning.h"
#include "modules/planning/planning_base.h"

using ::apollo::cyber::common::GetProtoFromFile;
using ::apollo::cyber::message::RawMessage;
using ::apollo::cyber::record::RecordMessage;
using ::apollo::cyber::record::RecordReader;
using ::apollo::cyber::record::RecordWriter;

using ::apollo::canbus::Chassis;
using ::apollo::common::Header;
using ::apollo::common::TrajectoryPoint;
using ::apollo::localization::LocalizationEstimate;
using ::apollo::perception::TrafficLightDetection;
using ::apollo::prediction::PredictionObstacles;
using ::apollo::routing::RoutingResponse;
using ::apollo::storytelling::Stories;

using ::apollo::planning::ADCTrajectory;
using ::apollo::planning::DependencyInjector;
using ::apollo::planning::LocalView;
using ::apollo::planning::OnLanePlanning;
using ::apollo::planning::PlanningBase;
using ::apollo::planning::PlanningConfig;
using ::apollo::planning_internal::PlanningData;

int main(int argc, char *argv[]) {
  auto init_start = std::chrono::steady_clock::now();

  ::apollo::cyber::Init("deft_icse_24");

  // Initialize Planning
  std::string flag_file_path = "/apollo/modules/planning/conf/planning.conf";
  google::SetCommandLineOption("flagfile", flag_file_path.c_str());
  google::ParseCommandLineFlags(&argc, &argv, true);

  FLAGS_test_base_map_filename = "base_map.bin";
  FLAGS_enable_reference_line_provider_thread = false;

  PlanningConfig config_;
  GetProtoFromFile("/apollo/modules/planning/conf/planning_config.pb.txt",
                   &config_);
  std::shared_ptr<DependencyInjector> injector_ =
      std::make_shared<DependencyInjector>();
  std::unique_ptr<PlanningBase> planning_ =
      std::unique_ptr<PlanningBase>(new OnLanePlanning(injector_));
  planning_->Init(config_);

  auto init_end = std::chrono::steady_clock::now();
  std::chrono::duration<double> init_elapsed = init_end - init_start;

  // DeFT
  std::chrono::duration<double> io_duration(0);
  std::chrono::duration<double> planning_duration(0);

  apollo::cyber::Clock::SetMode(apollo::cyber::proto::MODE_MOCK);
  apollo::cyber::Clock::SetNowInSeconds(0);

  const char* user = std::getenv("USER");
  if (user == nullptr) {
    std::cerr << "USER environment variable is not set. Exiting program." << std::endl;
    std::exit(EXIT_FAILURE);
  }

  std::string deft_tmp_dir = user != nullptr 
    ? "/home/" + std::string(user) + "/deft/testdata" 
    : "/apollo/modules/deft/testdata";

  int input_seq_num = 0;

  while (true) {
    std::cout << "DeFT Processing Frame " << input_seq_num << std::endl;
    auto frame_start = std::chrono::steady_clock::now();
    // check if 0_planning.bin exists
    std::string input_file_name =
        deft_tmp_dir + "/" + std::to_string(input_seq_num) + "/planning.bin";
    std::ifstream input_file(input_file_name);
    if (!input_file.good()) {
      break;
    }
    input_file.close();

    // load inputs to planning module
    RoutingResponse routing;
    Chassis chassis;
    LocalizationEstimate adc_position;
    PredictionObstacles prediction;
    TrafficLightDetection tld;
    Stories stories;
    ADCTrajectory planning;
    Header header;

    apollo::cyber::common::GetProtoFromFile(
        deft_tmp_dir + "/" + std::to_string(input_seq_num) + "/routing.bin",
        &routing);
    apollo::cyber::common::GetProtoFromFile(
        deft_tmp_dir + "/" + std::to_string(input_seq_num) + "/chassis.bin",
        &chassis);
    apollo::cyber::common::GetProtoFromFile(deft_tmp_dir + "/" +
                                                std::to_string(input_seq_num) +
                                                "/localization.bin",
                                            &adc_position);
    apollo::cyber::common::GetProtoFromFile(
        deft_tmp_dir + "/" + std::to_string(input_seq_num) + "/prediction.bin",
        &prediction);
    apollo::cyber::common::GetProtoFromFile(deft_tmp_dir + "/" +
                                                std::to_string(input_seq_num) +
                                                "/traffic_light.bin",
                                            &tld);
    // apollo::cyber::common::GetProtoFromFile(deft_tmp_dir + "/" +
    //                                             std::to_string(input_seq_num)
    //                                             +
    //                                             "/stories.bin",
    //                                         &stories);
    apollo::cyber::common::GetProtoFromFile(
        deft_tmp_dir + "/" + std::to_string(input_seq_num) + "/header.bin",
        &header);
    apollo::cyber::Clock::SetNowInSeconds(header.timestamp_sec());

    auto frame_io = std::chrono::steady_clock::now();

    LocalView local_view_;
    local_view_.routing = std::make_shared<RoutingResponse>(routing);
    local_view_.chassis = std::make_shared<Chassis>(chassis);
    local_view_.localization_estimate =
        std::make_shared<LocalizationEstimate>(adc_position);
    local_view_.prediction_obstacles =
        std::make_shared<PredictionObstacles>(prediction);
    local_view_.traffic_light = std::make_shared<TrafficLightDetection>(tld);
    local_view_.stories = std::make_shared<Stories>(stories);

    ADCTrajectory adc_trajectory_pb;
    planning_->RunOnce(local_view_, &adc_trajectory_pb);

    std::string output_file_name =
        deft_tmp_dir + "/" + std::to_string(input_seq_num) + "/deft.bin";

    apollo::cyber::common::SetProtoToBinaryFile(adc_trajectory_pb,
                                                output_file_name);
    // apollo::cyber::common::SetProtoToASCIIFile(adc_trajectory_pb,
    // output_file_name);

    auto frame_planning = std::chrono::steady_clock::now();
    auto io_elapsed = frame_io - frame_start;

    io_duration += (frame_io - frame_start);
    planning_duration += (frame_planning - frame_io);

    input_seq_num++;
  }

  auto final_end = std::chrono::steady_clock::now();
  std::chrono::duration<double> total_elapsed = final_end - init_start;

  std::cout << "stopped at input_seq_num: " << input_seq_num << std::endl;
  std::cout << "INIT TIME: " << init_elapsed.count() << " seconds" << std::endl;
  std::cout << "TOTAL TIME: " << total_elapsed.count() << " seconds"
            << std::endl;
  std::cout << "IO TIME: " << io_duration.count() << " seconds" << std::endl;
  std::cout << "PLANNING TIME: " << planning_duration.count() << " seconds"
            << std::endl;
  return 0;
}