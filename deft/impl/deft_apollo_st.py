from deft.impl.deft_apollo import DeFTApollo

S_EPSILON = 1e-6

S_TOLERANCE = 1e-3

DENSE_INTERVAL = 0.02  # trajectory_time_min_interval
SPARSE_INTERVAL = 0.1  # trajectory_time_max_interval
HIGH_DENSITY_PERIOD = 1.0  # trajectory_time_high_density_period


class DeFTApolloST(DeFTApollo):
    """
    DeFTApolloST reconstructs frames from records of on-lane planning,
    accounting for trajectory stitching.
    """

    @staticmethod
    def _init_point_index(pmsg) -> int:
        """
        Locate the planning init point index within the published trajectory.

        Args:
            pmsg: A planning message carrying at least one trajectory point.

        Returns:
            int: Index of the init point in ``pmsg.trajectory_point``.
        """
        tp = pmsg.trajectory_point

        if pmsg.is_replan:
            return 0

        from_grid = DeFTApolloST._seam_from_publish_grid(tp)
        if from_grid >= 0 and abs(tp[from_grid].path_point.s) <= S_TOLERANCE:
            return from_grid

        candidates = [k for k, p in enumerate(tp) if abs(p.path_point.s) <= S_EPSILON]
        if not candidates:
            candidates = [min(range(len(tp)), key=lambda k: abs(tp[k].path_point.s))]
        if len(candidates) == 1:
            return candidates[0]

        init_rel = pmsg.debug.planning_data.init_point.relative_time
        latency = pmsg.latency_stats.total_time_ms / 1e3
        return min(
            candidates,
            key=lambda k: abs(tp[k].relative_time - init_rel + latency),
        )

    @staticmethod
    def _seam_from_publish_grid(tp):
        """
        Locate the seam from the spacing of the published points.

        Args:
            tp: The published trajectory points.

        Returns:
            int: Index of the seam, or -1 when the trajectory has no sparse
            tail to measure from.
        """
        last_dense = len(tp) - 1
        while (
            last_dense > 0
            and tp[last_dense].relative_time - tp[last_dense - 1].relative_time
            > (DENSE_INTERVAL + SPARSE_INTERVAL) / 2
        ):
            last_dense -= 1

        if last_dense == len(tp) - 1:
            return -1

        seam_time = tp[last_dense].relative_time - HIGH_DENSITY_PERIOD
        return min(
            range(last_dense + 1),
            key=lambda k: abs(tp[k].relative_time - seam_time),
        )

    @staticmethod
    def _infer_tF(pmsg) -> float:
        """
        Derive the frame construction time tF from the init point's two clocks.

        Args:
            pmsg: A planning message carrying at least one trajectory point.

        Returns:
            float: The frame construction time tF.
        """
        index = DeFTApolloST._init_point_index(pmsg)
        init_rel = pmsg.debug.planning_data.init_point.relative_time
        return (
            pmsg.header.timestamp_sec
            + pmsg.trajectory_point[index].relative_time
            - init_rel
        )
