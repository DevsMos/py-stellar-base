# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
import base64
from typing import List
from xdrlib3 import Packer, Unpacker

from .constants import *
from .invoke_host_function_result_code import InvokeHostFunctionResultCode
from .sc_val import SCVal

__all__ = ["InvokeHostFunctionResult"]


class InvokeHostFunctionResult:
    """
    XDR Source Code::

        union InvokeHostFunctionResult switch (InvokeHostFunctionResultCode code)
        {
        case INVOKE_HOST_FUNCTION_SUCCESS:
            SCVal success<MAX_OPS_PER_TX>;
        case INVOKE_HOST_FUNCTION_MALFORMED:
        case INVOKE_HOST_FUNCTION_TRAPPED:
        case INVOKE_HOST_FUNCTION_RESOURCE_LIMIT_EXCEEDED:
            void;
        };
    """

    def __init__(
        self,
        code: InvokeHostFunctionResultCode,
        success: List[SCVal] = None,
    ) -> None:
        _expect_max_length = MAX_OPS_PER_TX
        if success and len(success) > _expect_max_length:
            raise ValueError(
                f"The maximum length of `success` should be {_expect_max_length}, but got {len(success)}."
            )
        self.code = code
        self.success = success

    @classmethod
    def from_invoke_host_function_success(
        cls, success: List[SCVal]
    ) -> "InvokeHostFunctionResult":
        return cls(
            InvokeHostFunctionResultCode.INVOKE_HOST_FUNCTION_SUCCESS, success=success
        )

    @classmethod
    def from_invoke_host_function_malformed(cls) -> "InvokeHostFunctionResult":
        return cls(InvokeHostFunctionResultCode.INVOKE_HOST_FUNCTION_MALFORMED)

    @classmethod
    def from_invoke_host_function_trapped(cls) -> "InvokeHostFunctionResult":
        return cls(InvokeHostFunctionResultCode.INVOKE_HOST_FUNCTION_TRAPPED)

    @classmethod
    def from_invoke_host_function_resource_limit_exceeded(
        cls,
    ) -> "InvokeHostFunctionResult":
        return cls(
            InvokeHostFunctionResultCode.INVOKE_HOST_FUNCTION_RESOURCE_LIMIT_EXCEEDED
        )

    def pack(self, packer: Packer) -> None:
        self.code.pack(packer)
        if self.code == InvokeHostFunctionResultCode.INVOKE_HOST_FUNCTION_SUCCESS:
            if self.success is None:
                raise ValueError("success should not be None.")
            packer.pack_uint(len(self.success))
            for success_item in self.success:
                success_item.pack(packer)
            return
        if self.code == InvokeHostFunctionResultCode.INVOKE_HOST_FUNCTION_MALFORMED:
            return
        if self.code == InvokeHostFunctionResultCode.INVOKE_HOST_FUNCTION_TRAPPED:
            return
        if (
            self.code
            == InvokeHostFunctionResultCode.INVOKE_HOST_FUNCTION_RESOURCE_LIMIT_EXCEEDED
        ):
            return

    @classmethod
    def unpack(cls, unpacker: Unpacker) -> "InvokeHostFunctionResult":
        code = InvokeHostFunctionResultCode.unpack(unpacker)
        if code == InvokeHostFunctionResultCode.INVOKE_HOST_FUNCTION_SUCCESS:
            length = unpacker.unpack_uint()
            success = []
            for _ in range(length):
                success.append(SCVal.unpack(unpacker))
            return cls(code=code, success=success)
        if code == InvokeHostFunctionResultCode.INVOKE_HOST_FUNCTION_MALFORMED:
            return cls(code=code)
        if code == InvokeHostFunctionResultCode.INVOKE_HOST_FUNCTION_TRAPPED:
            return cls(code=code)
        if (
            code
            == InvokeHostFunctionResultCode.INVOKE_HOST_FUNCTION_RESOURCE_LIMIT_EXCEEDED
        ):
            return cls(code=code)
        return cls(code=code)

    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> "InvokeHostFunctionResult":
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> "InvokeHostFunctionResult":
        xdr_bytes = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr_bytes)

    def __eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.code == other.code and self.success == other.success

    def __str__(self):
        out = []
        out.append(f"code={self.code}")
        out.append(f"success={self.success}") if self.success is not None else None
        return f"<InvokeHostFunctionResult [{', '.join(out)}]>"
