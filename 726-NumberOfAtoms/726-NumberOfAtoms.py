# Last updated: 6/4/2025, 9:21:52 PM
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        import collections

        def parse():
            n = len(formula)
            i = [0]

            def parse_atom():
                start = i[0]
                i[0] += 1
                while i[0] < n and formula[i[0]].islower():
                    i[0] += 1
                return formula[start:i[0]]

            def parse_num():
                if i[0] == n or not formula[i[0]].isdigit():
                    return 1
                start = i[0]
                while i[0] < n and formula[i[0]].isdigit():
                    i[0] += 1
                return int(formula[start:i[0]])

            stack = [collections.Counter()]
            while i[0] < n:
                if formula[i[0]] == '(':
                    i[0] += 1
                    stack.append(collections.Counter())
                elif formula[i[0]] == ')':
                    i[0] += 1
                    num = parse_num()
                    top = stack.pop()
                    for atom in top:
                        stack[-1][atom] += top[atom] * num
                else:
                    atom = parse_atom()
                    num = parse_num()
                    stack[-1][atom] += num
            
            return stack.pop()

        atom_counts = parse()
        result = []
        for atom in sorted(atom_counts):
            count = atom_counts[atom]
            if count > 1:
                result.append("{}{}".format(atom, count))
            else:
                result.append(atom)
        return ''.join(result)
