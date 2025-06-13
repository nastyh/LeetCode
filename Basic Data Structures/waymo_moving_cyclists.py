from dataclasses import dataclass
from typing import Iterable


@dataclass
class Cyclist:
  """
  Data for a cyclist at a point in time.
  Represents a single cyclist’s state at one point in time.
  id is id
  time: Timestamp (float, possibly seconds since start or epoch).
  x, y: 2D coordinates of the cyclist's position at that time.
  """

  id: str
  time: float
  x: float
  y: float

@dataclass
class Example:
  """
  Training example with recent position history for a set of cyclists.
  Represents a training example of cyclists' position history over time.
  valid: 2D list (time steps × cyclists) indicating if a value is present (e.g., sensor detected a cyclist).

    x: same shape, stores the x-coordinate.

    y: same shape, stores the y-coordinate.

    Think of it like a matrix per feature (valid/x/y) of shape [num_steps][max_cyclists].
  """

  valid: list[list[bool]]
  x: list[list[float]]
  y: list[list[float]]

  @property
  def num_steps(self) -> int:
    """
    Returns number of time steps (i.e., rows in the valid matrix).
    """
    return len(self.valid)

  @property
  def max_cyclists(self) -> int:
    """
    Returns number of cyclists tracked (i.e., columns).
    """
    return len(self.valid[0])

  @staticmethod
  def create_empty() -> 'Example':
    """
    Returns a 3-step example (e.g., 3 time steps) tracking 2 cyclists.

    All data is initialized to invalid (False) and position 0.0.
    """
    return Example(
        valid=[
            [False, False],
            [False, False],
            [False, False],
        ],
        x=[
            [0.0, 0.0],
            [0.0, 0.0],
            [0.0, 0.0],
        ],
        y=[
            [0.0, 0.0],
            [0.0, 0.0],
            [0.0, 0.0],
        ],
    )
  
  from typing import Iterable

def fill_example(
    example: Example, example_time: float, cyclists: Iterable[Cyclist]
) -> None:
    """
    O(c), num of cyclists
    O(m), m number of cyclists' columns in the matrix
    """
    # Step 1: Map cyclist IDs to column indices (assume fixed set of cyclists)
    # We'll assign the first N seen cyclist IDs to the N columns
    id_to_index = {}
    current_index = 0

    for c in cyclists:
        if c.id not in id_to_index and current_index < example.max_cyclists:
            id_to_index[c.id] = current_index
            current_index += 1

    # Step 2: Fill the example
    for c in cyclists:
        if c.id not in id_to_index:
            continue  # Skip unknown cyclists if more than max_cyclists

        j = id_to_index[c.id]
        dt = example_time - c.time  # How far in the past

        # Check if dt corresponds to a valid index in the history
        if dt < 0 or not dt.is_integer():
            continue  # Ignore future or non-discrete times

        i = int(dt)
        if 0 <= i < example.num_steps:
            example.valid[i][j] = True
            example.x[i][j] = c.x
            example.y[i][j] = c.y

example = Example.create_empty()
example_time = 10.0
cyclists = [
    Cyclist(id="A", time=10.0, x=1.0, y=1.0),
    Cyclist(id="A", time=9.0, x=0.5, y=1.1),
    Cyclist(id="B", time=8.0, x=2.0, y=2.0),
]
fill_example(example, example_time, cyclists)

