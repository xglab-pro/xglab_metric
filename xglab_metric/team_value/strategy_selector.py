from typing import Dict, List

from xglab_metric.ValuedEvent import ValuedEvent
from xglab_metric.team_value.KeepValue import KeepValue
from xglab_metric.team_value.TeamValueStrategyType import TeamValueStrategyType
from xglab_metric.team_value.TotalProbability import TotalProbability


def get_team_value_map(strategy: TeamValueStrategyType, valued_events: List[ValuedEvent]) -> Dict[str, float]:
    if strategy == TeamValueStrategyType.KeepValue:
        return KeepValue.get_team_value_map(valued_events)
    if strategy == TeamValueStrategyType.TotalProbability:
        return TotalProbability.get_team_value_map(valued_events)
    raise Exception(f'Unknown strategy {strategy}')
