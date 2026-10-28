class Node:
    def __new__(cls, *args):
        if cls is Node:
            raise TypeError("Cannot instantiate Node")
        
        return super().__new__(cls)

    def __repr__(self):
        lines = [f"{type(self).__name__}: "]

        for key, value in vars(self).items():
            lines.append(" " * 4 + str(key) + ": ")

            if isinstance(value, Node):
                for line in str(value).splitlines()[1:-1:]:
                    lines.append(" " * 8 + line)
            else:
                lines[-1] += str(value)
        
        return "\n" + "\n".join(lines) + "\n"