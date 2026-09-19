from pathlib import Path
from typing import Any
import json

from flintmc.nodes.definitions import (
  definitionT,
  FuncDef,
  TickDef,
  LoadDef,
)

from flintmc.nodes.statements import (
  stmtT,
  Assignment,
  FuncCall,
  Conditional,
  Repeat,
  Execute,
  Run,
  If,
  Elif,
  Else,
  ExecArg,
)

from flintmc.nodes.expression import (
  MathBinaryOp,
  MathNeg,
  LogicBinaryOp,
  LogicNot,
  Comparison,
  EntityProp,
)

from flintmc.utils import filter_by_type

def generate_files(ast: list, /, *, namespace: str = "minecraft") -> dict:
  """ Takes the AST and sorts the nodes into multiple files. """

  def sort_stmts(stmts: list[stmtT], /) -> dict:
    file_map: dict[Path, Any] = {}

    conditionals = filter_by_type(stmts, Conditional)
    executes = filter_by_type(stmts, Execute)
    repeats = filter_by_type(stmts, Repeat)

    for i, conditional in enumerate(conditionals):
      file_map[Path(f"if-{i}")] = conditional.if_stmt.stmts
    
      for j, elif_stmt in enumerate(conditional.elif_stmts):
        file_map[Path(f"elif-{i}-{j}")] = elif_stmt.stmts

      if conditional.else_stmt:
        file_map[Path(f"else-{i}")] = else_stmt.stmts

    for i, execute in enumerate(executes):
      file_map[Path(f"exec-{i}")] = execute.stmts

    for i, repeat in enumerate(repeats):
      file_map[Path(f"repeat-{i}")] = repeat.stmts

    return file_map

  def recursive_sort(
    dir_struct: dict[Path, definitionT | stmtT],
    stmts: list[stmtT],
    /,
    id: str,
    *,
    path: Path
  ):

    dir_struct[path / f"{id}.mcfunction"] = stmts

    for statement in stmts:
      for file_name, file_content in sort_stmts(stmts).items():
        dir_struct.update({
          path / f"{id}-subfuncs" / file_name: file_content
        })

        recursive_sort(
          dir_struct,
          file_content, 
          id=file_name,
          path=path / f"{id}-subfuncs"
        )

  dir_struct: dict[Path, str | stmtT] = {}

  tick_ids: list[str] = []
  load_ids: list[str] = []

  dir_struct[Path("data/math/context_float_provider/add.json")] = json.dumps({
    "type": "add",
    "inputs": [
      {
        "type": "storage",
        "storage": "math:temp_vars",
        "path": "input_1"
      },
      {
        "type": "storage",
        "storage": "math:temp_vars",
        "path": "input_2"
      }
    ]
  })

  dir_struct[Path("data/math/context_float_provider/sub.json")] = json.dumps({
    "type": "sub",
    "left": {
      "type": "storage",
      "storage": "math:temp_vars",
      "path": "input_1"
    },
    "right": {
      "type": "storage",
      "storage": "math:temp_vars",
      "path": "input_2"
    }
  })

  dir_struct[Path("data/math/context_float_provider/mul.json")] = json.dumps({
    "type": "mul",
    "inputs": [
      {
        "type": "storage",
        "storage": "math:temp_vars",
        "path": "input_1"
      },
      {
        "type": "storage",
        "storage": "math:temp_vars",
        "path": "input_2"
      }
    ]
  })

  dir_struct[Path("data/math/context_float_provider/div.json")] = json.dumps({
    "type": "div",
    "left": {
      "type": "storage",
      "storage": "math:temp_vars",
      "path": "input_1"
    },
    "right": {
      "type": "storage",
      "storage": "math:temp_vars",
      "path": "input_2"
    }
  })

  dir_struct[Path("data/math/context_float_provider/pow.json")] = json.dumps({
    "type": "pow",
    "base": {
      "type": "storage",
      "storage": "math:temp_vars",
      "path": "input_1"
    },
    "exponent": {
      "type": "storage",
      "storage": "math:temp_vars",
      "path": "input_2"
    }
  })

  for definition in ast:
    if isinstance(definition, TickDef):
      tick_ids.append(definition.id)

    if isinstance(definition, LoadDef):
      load_ids.append(definition.id)

    recursive_sort(
      dir_struct,
      definition.stmts,
      id=definition.id,
      path=Path(f"data/{namespace}/function")
    )
    
  dir_struct[Path("data/minecraft/tags/function/tick.json")] = json.dumps({
    "values": tick_ids
  })

  dir_struct[Path("data/minecraft/tags/function/load.json")] = json.dumps({
    "values": load_ids
  })

  return dir_struct