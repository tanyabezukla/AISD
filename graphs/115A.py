class Solution:
    def minimum_groups(self, managers: list[int]) -> int:
        n = len(managers)
        children = [[] for _ in range(n)]
        roots = []

        for employee, manager in enumerate(managers):
            if manager == -1:
                roots.append(employee)
            else:
                children[manager - 1].append(employee)

        max_depth = 0
        stack = [(root, 1) for root in roots]

        while stack:
            employee, depth = stack.pop()
            max_depth = max(max_depth, depth)

            for subordinate in children[employee]:
                stack.append((subordinate, depth + 1))

        return max_depth


def test_solution() -> None:
    solution = Solution()
    assert solution.minimum_groups([-1]) == 1
    assert solution.minimum_groups([-1, 1, 2, 1, -1]) == 3
    assert solution.minimum_groups([-1, 1, 1, 2, 2]) == 3
    print("All test cases passed!")


def main() -> None:
    n = int(input())
    managers = [int(input()) for _ in range(n)]
    solution = Solution()
    print(solution.minimum_groups(managers))


test_solution()
main()
