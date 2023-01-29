from typing import Self
from dataclasses import dataclass


@dataclass
class NumIterator:
    max_: int 
    num: int = 0
    

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if self.num >= self.max_:
            raise StopIteration
        self.num += 1
        return self.num


def main() -> None:

    for i in NumIterator(7,4):
        print(i)

if __name__ == '__main__':
    main()


    
