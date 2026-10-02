class NodeType:
  def __repr__(self) -> str:
    str_repr = f"{type(self).__name__}:"

    for attr, value in vars(self).items():
      str_repr.append(f"  {attr}:\n    {value}")

    return str_repr