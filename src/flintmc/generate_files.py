from pathlib import Path
from typing import Any
import json

from flintmc.nodes import (
  definitionT,
  FuncDef,
  TickDef,
  LoadDef,
  stmtT,
  Conditional,
  Repeat,
  Execute,
)

def generate_files(
  ast: list[definitionT],
  namespace: str = "minecraft",
  /
) -> dict[Path, str | list[stmtT]]:

  """Takes the AST and sorts the nodes into multiple files. Also
  returns 3 lists of definitions, one for each type.
  """

  def generate_subfuncs(
    stmts: list[stmtT],
    path: Path,
    /
  ) -> dict[Path, list[stmtT]]:

    subfuncs: dict[Path, list[stmtT]] = {}

    for stmt_idx, stmt in enumerate(stmts):
      if isinstance(stmt, Conditional):
        subfuncs[path / f"if-{stmt_idx}"] = stmt.if_stmt.stmts

        if stmt.else_stmt:
          subfuncs[path / f"else-{stmt_idx}"] = stmt.else_stmt.stmts

      elif isinstance(stmt, Execute):
        subfuncs[path / f"execute-{stmt_idx}"] = stmt.stmts

      elif isinstance(stmt, Repeat):
        subfuncs[path / f"repeat-{stmt_idx}"] = stmt.stmts

    return subfuncs

  def construct_funcs(
    dir_struct: dict[Path, str | list[stmtT]],
    stmts: list[stmtT],
    id: str,
    path: Path,
    /
  ):

    # Add the function to dir_struct
    dir_struct[path / f"{id}.mcfunction"] = stmts

    subfuncs = generate_subfuncs(stmts, path / f"{id}_subfuncs")

    # Add the subfunctions to dir_struct
    dir_struct.update(subfuncs)

    for path, subfunc_stmts in subfuncs.items():

      # For every compound statement in the subfunction, set the path
      # property to its path
      for subfunc_stmt in subfunc_stmts:
        if isinstance(subfunc_stmt, (Conditional, Execute, Repeat)):
          subfunc_stmt.path = path

      construct_funcs(
        dir_struct,
        subfunc_stmts, 
        path,
        path / f"{id}-subfuncs"
      )

  dir_struct: dict[Path, str | list[stmtT]] = {}

  func_defs = [
    definition for definition in ast
    if isinstance(definition, FuncDef)
  ]

  tick_defs = [
    definition for definition in ast
    if isinstance(definition, TickDef)
  ]

  load_defs = [
    definition for definition in ast
    if isinstance(definition, LoadDef)
  ]

  math_float_provider_path = Path("data", "math", "context_float_provider")
  function_tags_path = Path("data", "minecraft", "tags", "function")

  dir_struct[Path("pack.mcmeta")] = json.dumps({
    "pack": {
      "description": "",
      "min_format": 121,
      "max_format": 999
    }
  })

  dir_struct[math_float_provider_path / "add.json"] = json.dumps({
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

  dir_struct[math_float_provider_path / "sub.json"] = json.dumps({
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

  dir_struct[math_float_provider_path / "mul.json"] = json.dumps({
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

  dir_struct[math_float_provider_path / "div.json"] = json.dumps({
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

  dir_struct[math_float_provider_path / "pow.json"] = json.dumps({
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
    if definition == None:
      continue
      
    construct_funcs(
      dir_struct,
      definition.stmts,
      definition.resource_loc.id,
      Path("data", definition.resource_loc.namespace, "function")
    )
    
  dir_struct[function_tags_path / "tick.json"] = json.dumps({
    "values": [str(tick_def.resource_loc) for tick_def in tick_defs]
  })

  dir_struct[function_tags_path / "load.json"] = json.dumps({
    "values": [str(load_def.resource_loc) for load_def in load_defs]
  })

  return {
    "dir_struct": dir_struct,
    "func_defs": func_defs,
    "tick_defs": tick_defs,
    "load_defs": load_defs
  }