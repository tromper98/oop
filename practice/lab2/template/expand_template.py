import os.path
from typing import List, Dict, Optional, Iterable, Tuple, Set
from argparse import ArgumentParser


class ProgramArguments:
    def __init__(self, input_file: str, output_file: str, params: List[str]):
        self.input_file: str = input_file
        self.output_file: str = output_file
        self.params: Optional[Dict[str, str]] = self._parse_params(params)

    @staticmethod
    def _parse_params(params: List[str]) -> Optional[Dict[str, str]]:
        if len(params) % 2 != 0:
            return None

        dictionary: Dict[str, str] = dict()
        for i in range(0, len(params) - 1, 2):

            if params[i] != '':
                dictionary[params[i]] = params[i+1]
        return dictionary


class Node:
    def __init__(self):
        self.next_nodes: Dict[str, Node] = {}
        self.patterns: List[str] = []
        self.suffix_link = None


class ReplacementsList:
    replacements: List[Tuple[int, str]]
    _current_replacement_pos: int
    _replacements_len: int

    def __init__(self, replacements: List[Tuple[int, str]]) -> None:
        self.replacements = replacements
        self._current_replacement_pos = 0
        self._replacements_len = len(replacements)

    def get_replacements_for_position(self, template_pos: int) -> List[str]:
        first_pos: int = self._current_replacement_pos

        while self.replacements[first_pos][0] != template_pos:
            first_pos += 1

        last_pos: int = first_pos + 1
        for i in range(first_pos, self._replacements_len):
            pos, _ = self.replacements[i]
            if pos != template_pos or pos == self._replacements_len:
                last_pos = i
                break

        self._current_replacement_pos = last_pos
        return [replacement for _, replacement in self.replacements[first_pos: last_pos]]

    def get_replacements_positions(self) -> Set[int]:
        return set([pos for pos, _ in self.replacements])

class AhoKorasikTree:
    def __init__(self, patterns: List[str]):
        self._root = self._init_tree(patterns)

    #row - заменить
    #find_all_patterns
    def find_all_patterns(self, template: str) -> List[Tuple[int, str]]:
        node: Node = self._root
        patterns: List[Tuple[int, str]] = []
        for i in range(len(template)):
            while node is not None and template[i] not in node.next_nodes:
                node: Node = node.suffix_link
            if node is None:
                node = self._root
                continue
            node = node.next_nodes[template[i]]
            for pattern in node.patterns:
                data: List[Tuple[int, str]] = [(i - len(pattern) + 1, pattern)]
                patterns.extend(data)
        return sorted(patterns, key=lambda x: x[0])

    def _init_tree(self, patterns: List[str]) -> Node:
        root: Node = self._create_tree(patterns)
        return self._fill_tree(root)

    @staticmethod
    def _create_tree(patterns: List[str]) -> Node:
        root: Node = Node()

        for pattern in patterns:
            node: Node = root
            for symbol in pattern:
                node = node.next_nodes.setdefault(symbol, Node())
                node.suffix_link = root
            node.patterns.append(pattern)
        return root

    @staticmethod
    def _fill_tree(root: Node) -> Node:
        nodes: List[Node] = [node for node in root.next_nodes.values()]

        while len(nodes) > 0:
            current_node: Node = nodes.pop(0)

            for key, link_node in current_node.next_nodes.items():
                nodes.append(link_node)
                suffix_node: Node = current_node.suffix_link

                while suffix_node is not None and key not in suffix_node.next_nodes:
                    suffix_node = suffix_node.suffix_link

                link_node.suffix_link = suffix_node.next_nodes[key] if suffix_node else root
                link_node.patterns += link_node.suffix_link.patterns
        return root


def parse_command_line():
    parser = ArgumentParser()
    parser.add_argument('input_file', help='file path to input file', type=str)
    parser.add_argument('output_file', help='file path to output file', type=str)
    parser.add_argument('-l', nargs='+', help='list of pairs [param, value] which will replaced', required=True)

    args = parser.parse_args()
    return ProgramArguments(args.input_file, args.output_file, args.l)


def file_iterator(file_path: str) -> Iterable:
    with open(file_path, 'r', encoding='utf-8') as file:
        for row in file:
            yield row


#row переименовать в template
def expand_template(template: str, params: Dict[str, str], pattern_tree: AhoKorasikTree) -> str:

    replacements: ReplacementsList = ReplacementsList(pattern_tree.find_all_patterns(template))
    replacement_positions: Set[int] = replacements.get_replacements_positions()

    current_template_pos: int = 0

    expanded_template: str = '' #result_str или expanded_template
    while current_template_pos < len(template):
        if current_template_pos not in replacement_positions:
            expanded_template += template[current_template_pos]
            current_template_pos += 1
            continue

        possible_patterns: List[str] = replacements.get_replacements_for_position(current_template_pos)
        replacement: str = max(possible_patterns, key=len)

        expanded_template += params[replacement]
        current_template_pos += len(replacement)
    return expanded_template


def main():
    args: ProgramArguments = parse_command_line()

    if not args.params:
        print('Not enough params were given')
        return

    if not os.path.exists(args.input_file):
        print(f'File {args.input_file} doesn\'t found')
        return

    patterns = [key for key in args.params.keys()]
    aho_korasik_tree: AhoKorasikTree = AhoKorasikTree(patterns)

    with open(args.output_file, 'w', encoding='utf-8') as file:
        for row in file_iterator(args.input_file):
            expanded_template: str = expand_template(row, args.params, aho_korasik_tree)
            file.write(expanded_template)


if __name__ == '__main__':
    main()
