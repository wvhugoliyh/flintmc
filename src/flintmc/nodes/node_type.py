class NodeType:
  def __repr__(self) -> str:
    repr_lines = ["", f"{type(self).__name__}:", ""]

    for key, value in vars(self).items():
      repr_lines.append(f"  {key}:")

      if isinstance(value, NodeType):
        value_lines = str(value).splitlines()
        repr_lines.extend(map(lambda line: f"    {line}", value_lines[1::]))

      else:
        repr_lines[-1] = f"{repr_lines[-1]} {value}"

    return "\n".join(repr_lines)