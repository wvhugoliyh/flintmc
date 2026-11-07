from typing import Literal, TypeVar
from uuid import UUID

from lark import Transformer, v_args

from flintmc.nodes import (
    ArrayItem,
    Assignable,
    Assignment,
    BinaryOp,
    Comparator,
    Coordinate,
    Definition,
    FuncCall,
    FuncDef,
    NBTLocation,
    Property,
    Raw,
    ResourceLocation,
    Statement,
    TargetSelector,
    UnaryOp,
    Value,
)

T = TypeVar("T")

@v_args(inline=True)
class FlintParser(Transformer):
    def start(self, *definitions: Definition) -> list[Definition]:
        return list(definitions)


    def func_def(
            self, func: ResourceLocation, params: list[str],
            statements: list[Statement]) -> FuncDef:
        return FuncDef(func, params, statements)


    def items(self, *items: T) -> list[T]:
        return list(items)

    def code_block(self, *statements: Statement) -> list[Statement]:
        return list(statements)


    def assignment(self, variable: Assignable, value: Value) -> Assignment:
        return Assignment(variable, value)

    def func_call(
            self, function: ResourceLocation, args: list[Value]) -> FuncCall:
        return FuncCall(function, args)


    def variable(self, id: str) -> Property:
        return Property(ResourceLocation("minecraft", "vars"), id)

    def nbt(self, nbt_location: NBTLocation, id: str) -> Property:
        return Property(nbt_location, id)

    def map_property(self, map: Value, property_id: str) -> Property:
        return Property(map, property_id)

    def array_item(self, array: Value, index: Value) -> ArrayItem:
        return ArrayItem(array, index)

    def array(self, items: list[Value]) -> list[Value]:
        return items

    def map(self, kv_pairs: list[tuple[str, Value]]) -> dict[str, Value]:
        return dict(kv_pairs)

    def key_value_pair(self, key: str, value: Value) -> tuple[str, Value]:
        return (key, value)

    def disjunction(self, operand_1: Value, operand_2: Value) -> BinaryOp:
        return BinaryOp(operand_1, "||", operand_2)

    def conjunction(self, operand_1: Value, operand_2: Value) -> BinaryOp:
        return BinaryOp(operand_1, "&&", operand_2)

    def negation(self, operand: Value) -> UnaryOp:
        return UnaryOp("!", operand)

    def comparison(
            self, comparand_1: Value, comparator: Comparator,
            comparand_2: Value) -> BinaryOp:
        return BinaryOp(comparand_1, comparator, comparand_2)

    def sum(
            self, operand_1: Value, operator: Literal["+", "-"],
            operand_2: Value) -> BinaryOp:
        return BinaryOp(operand_1, operator, operand_2)

    def term(
            self, operand_1: Value, operator: Literal["*", "/"],
            operand_2: Value) -> BinaryOp:
        return BinaryOp(operand_1, operator, operand_2)

    def signed_power(
            self, operator: Literal["+", "-"], operand: Value) -> Value:
        return operand if operator == "+" else UnaryOp("-", operand)

    def power(self, operand_1: Value, operand_2: Value) -> BinaryOp:
        return BinaryOp(operand_1, "^", operand_2)


    def resource_location(
            self, namespace: str, id: str) -> ResourceLocation:
        return ResourceLocation(namespace, id)

    def coordinate(self, x: Value, y: Value, z: Value) -> Coordinate:
        return Coordinate(x, y, z)

    
    def ID(self, token) -> str:
        return str(token)

    def RAW(self, token) -> Raw:
        return Raw(token)

    def INT_LITERAL(self, token) -> int:
        return int(token)

    def FLOAT_LITERAL(self, token) -> float:
        return float(token)

    def BOOLEAN_LITERAL(self, token) -> bool:
        return str(token) == "True"

    def STRING_LITERAL(self, token) -> str:
        return str(token).strip("\"'")

    def SIGN(self, token) -> str:
        return str(token)

    def MUL_OP(self, token) -> str:
        return str(token)

    def COMPARATOR(self, token) -> str:
        return str(token)

    def UUID(self, token) -> UUID:
        return UUID(str(token))

    def TARGET_SELECTOR(self, token) -> TargetSelector:
        return TargetSelector(token[1])