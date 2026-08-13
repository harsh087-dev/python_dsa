class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        def solve(i):
            if i > n:
                return

            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))

            solve(i + 1)

        solve(1)
        return result