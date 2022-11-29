from typing import Sequence, Union

from .base import BaseScValAlias
from ..xdr import SCVal, SCValType, SCVec, SCObject, SCObjectType

__all__ = ["Vec"]


class Vec(BaseScValAlias):
    def __init__(self, vec: Sequence[Union[SCVal, BaseScValAlias]]):
        self.vec = vec

    def _to_xdr_sc_val(self) -> SCVal:
        return SCVal(
            SCValType.SCV_OBJECT,
            obj=SCObject(
                SCObjectType.SCO_VEC,
                vec=SCVec(
                    [
                        sc_val._to_xdr_sc_val()
                        if isinstance(sc_val, BaseScValAlias)
                        else sc_val
                        for sc_val in self.vec
                    ]
                ),
            ),
        )
