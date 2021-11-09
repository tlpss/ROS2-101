from typing import Any


class Fibonacci:
    def __init__(self) -> None:
        self.a = 0
        self.b = 1

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.a, self.b = self.b, self.a + self.b
        return self.b
