from typing import TypedDict, Optional

import xglab_metric.enums as enums


class Event(TypedDict):
    uuid: str
    type: enums.EventType
    matchId: int
    teamId: int
    isHomeTeam: bool
    playerId: Optional[int]
    minute: int
    expandedMinute: int
    second: int
    expandedSeconds: int
    period: enums.Period
    order: int
    dependentChainId: int
    isTouch: bool
    successful: bool
    timeFrameUuid: Optional[str]
    passType: Optional[enums.PassType]
    passDestination: Optional[enums.PassDestination]
    cross: Optional[bool]
    startX: Optional[float]
    startY: Optional[float]
    startSquare30: Optional[int]
    endX: Optional[float]
    endY: Optional[float]
    endZ: Optional[float]
    endSquare30: Optional[int]
    angle: Optional[float]
    length: Optional[float]
    positionName: Optional[enums.DetailedPositionName]
    generalPositionName: Optional[enums.GeneralPositionName]
    bodyPart: Optional[enums.BodyPart]
    saveType: Optional[enums.SaveType]
    shotResult: Optional[enums.ShotResult]
    errorResult: Optional[enums.ErrorResult]
    cardType: Optional[enums.CardType]
    cardReason: Optional[enums.CardReason]
    foulType: Optional[enums.FoulType]
    shotType: Optional[enums.ShotType]
    blocked: Optional[bool]
    bigChance: Optional[bool]
    assisted: Optional[bool]
    freeKick: Optional[bool]
    intentionalAssist: Optional[bool]
    chippedPass: Optional[bool]
    layOff: Optional[bool]
    indirectFreeKick: Optional[bool]
    isShotAssist: Optional[bool]
    relatedPlayerId: Optional[int]
    isOverRun: Optional[bool]
    saveResult: Optional[enums.SaveResult]
    formationName: Optional[enums.FormationName]
