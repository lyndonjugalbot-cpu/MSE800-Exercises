class Matrix:
    """A 2D matrix backed by a list of lists, with multiplication support."""

    def __init__(self, data):
        if not data or not all(isinstance(row, list) for row in data):
            raise ValueError("Matrix data must be a non-empty 2D list.")
        if len({len(row) for row in data}) != 1:
            raise ValueError("All rows must have the same number of columns.")

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def multiply(self, other):
        """Return self * other as a new Matrix."""
        if not isinstance(other, Matrix):
            raise TypeError("Can only multiply by another Matrix.")
        if self.cols != other.rows:
            raise ValueError(
                f"Incompatible shapes: {self.rows}x{self.cols} and "
                f"{other.rows}x{other.cols}. "
                f"Columns of M1 ({self.cols}) must equal rows of M2 ({other.rows})."
            )

        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]
        return Matrix(result)

    # Enables the * operator:  m1 * m2
    def __mul__(self, other):
        return self.multiply(other)

    def __str__(self):
        width = max(len(str(v)) for row in self.data for v in row)
        return "\n".join(
            "[ " + "  ".join(str(v).rjust(width) for v in row) + " ]"
            for row in self.data
        )


def main():
    # M1 size: 2x3
    m1 = Matrix([
        [1, 2, 3],
        [4, 5, 6],
    ])

    # M2 size: 3x2
    m2 = Matrix([
        [10, 11],
        [20, 21],
        [30, 31],
    ])

    product = m1 * m2

    print("M1:")
    print(m1)
    print("\nM2:")
    print(m2)
    print(f"\nM1 ({m1.rows}x{m1.cols}) * M2 ({m2.rows}x{m2.cols}) = "
          f"{product.rows}x{product.cols}:")
    print(product)


if __name__ == "__main__":
    main()
