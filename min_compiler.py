#Georgia Kalitsi 3238 --- cse63238
#Vaia Vanesa Tsinoudi 4004 --- cse64004

import sys

class lex():

    def __init__(self):
        self.lines = 0
        self.columns = 0
        self.id = ""
        self.id_value = ""
        self.digit = ""
        self.file_lines = []
        self.num_of_lines = 0
        self.id_limit = 0

    def set_file_lines(self, filename):
        try:
            file = open(filename, "r")
        except FileNotFoundError:
            print("File doesn't exist...\n")
            sys.exit()
        self.file_lines = file.readlines()
        self.set_num_of_lines()

    def set_num_of_lines(self):
        self.num_of_lines=len(self.file_lines)

    def get_line(self):
        return self.lines + 1

    def get_id_value(self):
        return self.id_value

    def return_token(self):
        while self.check_line_limit():
            while self.check_column_limit():
                if self.is_letter():
                    self.id += self.file_lines[self.lines][self.columns]
                    self.id_limit += 1
                    self.columns += 1
                    self.find_id()
                    self.id_limit = 0
                    return self.check_commited_word()
                if self.is_digit():
                    self.digit += self.file_lines[self.lines][self.columns]
                    self.columns += 1
                    return self.find_digit()
                punctuation = self.is_punctuation()
                if punctuation != "not_punctuation" and\
                    punctuation != "line_comment" and\
                    punctuation != "block_comment":
                    self.columns += 1
                    return punctuation
                # elif ord(self.file_lines[self.lines][self.columns]) == 10: #/n
                #     break
                self.columns += 1
            self.lines += 1
            self.columns = 0

    def check_line_limit(self):
        if self.lines < self.num_of_lines:
            return True
        return False

    def check_column_limit(self):
        if self.columns < len(self.file_lines[self.lines]):
            return True
        return False

    def find_id(self):
        while self.check_column_limit():  #orio stiles
            if self.is_letter():
                self.id += self.file_lines[self.lines][self.columns]
                self.id_limit += 1
                self.check_id_limit()
                self.columns+=1
            elif self.is_digit():
                self.id += self.file_lines[self.lines][self.columns]
                self.id_limit += 1
                self.check_id_limit()
                self.columns+=1
            else:
                break

    def check_id_limit(self):
        if self.id_limit > 30:
            print("Line: " + str(self.lines) + ", id's length can't be more" +
                    " than 30\n")
            sys.exit()

    def find_digit(self):
        while self.check_column_limit():
            if self.is_digit():
                self.digit += self.file_lines[self.lines][self.columns]
            else:
                self.id_value = self.digit
                break
            if not self.check_digit_limit():
                print("Not valid number\n")
                sys.exit()
            self.columns+=1
        self.digit = ""
        return "constanttk"

    def check_digit_limit(self):
        if int(self.digit) < 32767 and int(self.digit) > -32767:
            return True
        return False

    def is_letter(self):
        if self.file_lines[self.lines][self.columns].isalpha():
            return True
        return False

    def is_digit(self):
        if ord(self.file_lines[self.lines][self.columns]) >= 48 and\
            ord(self.file_lines[self.lines][self.columns]) <= 57:
            return True
        return False

    def check_commited_word(self):
        self.id_value = self.id
        if self.id == "program":
            self.id = ""
            return "programtk"
        elif self.id == "declare":
            self.id = ""
            return "declaretk"
        elif self.id == "if":
            self.id = ""
            return "iftk"
        elif self.id == "else":
            self.id = ""
            return "elsetk"
        elif self.id == "then":
            self.id = ""
            return "thentk"
        elif self.id == "while":
            self.id=""
            return "whiletk"
        elif self.id == "forcase":
            self.id = ""
            return "forcasetk"
        elif self.id == "not":
            self.id = ""
            return "nottk"
        elif self.id == "function":
            self.id = ""
            return "functiontk"
        elif self.id == "input":
            self.id = ""
            return "inputtk"
        elif self.id == "doublewhile":
            self.id = ""
            return "doublewhiletk"
        elif self.id == "incase":
            self.id = ""
            return "incasetk"
        elif self.id ==  "and":
            self.id = ""
            return "andtk"
        elif self.id == "procedure":
            self.id = ""
            return "proceduretk"
        elif self.id == "print":
            self.id = ""
            return "printtk"
        elif self.id == "loop":
            self.id = ""
            return "looptk"
        elif self.id == "when":
            self.id = ""
            return "whentk"
        elif self.id == "or":
            self.id = ""
            return "ortk"
        elif self.id == "exit":
            self.id = ""
            return "exittk"
        elif self.id == "default":
            self.id = ""
            return "defaulttk"
        elif self.id == "return":
            self.id = ""
            return "returntk"
        elif self.id == "in":
            self.id = ""
            return "intk"
        elif self.id == "inout":
            self.id = ""
            return "inouttk"
        elif self.id == "call":
            self.id = ""
            return "calltk"
        self.id = ""
        return "idtk"

    def is_punctuation(self):
        if ord(self.file_lines[self.lines][self.columns]) == 43:
            self.id_value = "+"
            return "plustk"
        elif ord(self.file_lines[self.lines][self.columns]) == 45:
            self.id_value = "-"
            return "minustk"
        elif ord(self.file_lines[self.lines][self.columns]) == 42:
            self.id_value = "*"
            return "multiplytk"
        elif ord(self.file_lines[self.lines][self.columns]) == 47:
            if self.check_line_comment():
                print("Line comment\n")
                return "line_comment"
            if self.check_block_comment():
                print("Block comment\n")
                return "block_comment"
            self.id_value = "/"
            return "dividetk"
        elif ord(self.file_lines[self.lines][self.columns]) == 60:
            if self.check_greater_or_less_equal():
                self.id_value = "<="
                return "lessequaltk"
            if self.check_nottk():
                return "not"
                return "nottk"
            self.id_value = "<"
            return "lesstk"
        elif ord(self.file_lines[self.lines][self.columns]) == 62:
            if self.check_greater_or_less_equal():
                self.id_value = ">="
                return "greaterequaltk"
            return "greatertk"
        elif ord(self.file_lines[self.lines][self.columns]) == 61:
            self.id_value = "="
            return "equaltk"
        elif ord(self.file_lines[self.lines][self.columns]) == 59:
            self.id_value = ";"
            return "questiontk"
        elif ord(self.file_lines[self.lines][self.columns]) == 44:
            self.id_value = ","
            return "commatk"
        elif ord(self.file_lines[self.lines][self.columns]) == 58:
            if self.check_assigmenttk():
                self.id_value = ":="
                return "assignmenttk"
            self.id_value = ":"
            return "colontk"
        elif ord(self.file_lines[self.lines][self.columns]) == 40:
            self.id_value = "("
            return "left_round_brackettk"
        elif ord(self.file_lines[self.lines][self.columns]) == 41:
            self.id_value = ")"
            return "right_round_brackettk"
        elif ord(self.file_lines[self.lines][self.columns]) == 91:
            self.id_value = "["
            return "left_square_brackettk"
        elif ord(self.file_lines[self.lines][self.columns]) == 93:
            self.id_value = "]"
            return "right_square_brackettk"
        elif ord(self.file_lines[self.lines][self.columns]) == 123:
            self.id_value = "{"
            return "left_curly_brackettk"
        elif ord(self.file_lines[self.lines][self.columns]) == 125:
            self.id_value = "}"
            return "right_curly_brackettk"
        return "not_punctuation"

    def check_assigmenttk(self):
        self.columns += 1
        if self.check_column_limit():
            if ord(self.file_lines[self.lines][self.columns]) == 61:
                return True
        self.columns -= 1
        return False

    def check_greater_or_less_equal(self):
        self.columns += 1
        if self.check_column_limit():
            if ord(self.file_lines[self.lines][self.columns]) == 61:
                return True
        self.columns -= 1
        return False

    def check_nottk(self):
        self.columns += 1
        if self.check_column_limit():
            if ord(self.file_lines[self.lines][self.columns]) == 62:
                return True
        self.columns -= 1
        return False

    def check_line_comment(self):
        self.columns += 1
        if self.check_column_limit():
            if ord(self.file_lines[self.lines][self.columns]) == 47:
                while self.check_column_limit():
                    self.columns += 1
                return True
        self.columns -= 1
        return False

    def check_block_comment(self):
        self.columns += 1
        if self.check_column_limit():
            if ord(self.file_lines[self.lines][self.columns]) == 42:
                while self.check_line_limit():
                    self.columns += 1
                    while self.check_column_limit():
                        if ord(self.file_lines[self.lines][self.columns]) == 42:
                            self.columns += 1
                            if self.check_column_limit():
                                if ord(self.file_lines[self.lines]\
                                            [self.columns]) == 47:
                                    return True
                                else:
                                    self.columns -= 1
                        self.columns += 1
                    self.columns = -1
                    self.lines += 1
        return False

class yac():

    def __init__(self):
        self.lex = ""
        self.token = ""
        self.semi_code = semi_code()
        self.op = operation()
        self.left = ""
        self.rel = ""
        self.right = ""
        self.symbol_table_list = []
        self.nesting_level = 0
        self.function_call = ""
        self.function_name_for_table = ""
        self.function_open = 0
        self.not_boolean = False
        self.writer = semi_code_output_file()
        self.writer_to_c = semi_code_c_file()
        self.functions_name = []
        self.read_semi_code = None

    def set_file(self, file):
        self.lex = lex()
        self.lex.set_file_lines(file)

    def set_first_token(self):
        self.token = self.lex.return_token()

    def get_function(self, x):
        for function in self.symbol_table_list:
            if function.get_function_name() == x:
                return function
        print("Error: Not valid function name: " + str(x))
        sys.exit()
        return None

    def program(self):
        if self.token == "programtk":
            self.token = self.lex.return_token()
            id = self.lex.get_id_value()
            self.functions_name.append(id)
            if self.token == "idtk":
                function = symbol_table(self.nesting_level)
                self.function_name_for_table = self.lex.get_id_value()
                function.set_function_name(self.lex.get_id_value())
                self.symbol_table_list.append(function)
                self.token = self.lex.return_token()
                if self.token == "left_curly_brackettk":
                    self.token = self.lex.return_token()
                    self.block()
                    self.semi_code.gen_quad("halt", "_", "_", "_")
                    self.semi_code.next_quad()
                    self.semi_code.gen_quad("end_block", id, "_", "_")
                    self.semi_code.next_quad()
                    self.semi_code.print_all_quads(self.writer)
                    for i in range(0, self.semi_code.get_temp_var() + 1):
                        self.writer_to_c.add_variable("T_" + str(i))
                    for function in self.symbol_table_list:
                        function.print_function()
                    self.writer_to_c.fill_c_file(self.semi_code.get_all_quads())
                    self.read_semi_code = read_semi_code(self.semi_code.\
                                        get_all_quads(), self.symbol_table_list)
                    self.read_semi_code.read_quads()
                    if self.token == "right_curly_brackettk":
                        print("Your program is compiled succesfully!\n")
                        sys.exit()
                    else:
                        print("Line: " + str(self.lex.get_line()) +
                                "\nSyntax Error: Expected '}' after block\n")
                        sys.exit()
                else:
                    print("Line: " + str(self.lex.get_line()) +
                                "\nSyntax Error: Expected '}' before block\n")
                    sys.exit()
            else:
                print("Line: " + str(self.lex.get_line()) + " Expected id\n")
                sys.exit()

    def block(self):
        self.declarations()
        self.subprograms()
        self.semi_code.gen_quad("begin_block", self.functions_name[-1], "_", "_")
        self.semi_code.next_quad()
        self.statements()

    def declarations(self):
        while self.token == "declaretk":
            self.token = self.lex.return_token()
            self.varlist()
            if self.token == "questiontk":
                self.token = self.lex.return_token()
            else:
                print("Line: " + str(self.lex.get_line()) +
                        "\nSyntax Error: Expected ';' after declaration\n")
                sys.exit()

    def varlist(self):
        if self.token == "idtk":
            function = self.get_function(self.function_name_for_table)
            function.add_variable(self.lex.get_id_value())
            function.set_entity(self.lex.get_id_value())
            self.writer_to_c.add_variable(self.lex.get_id_value())
            self.token = self.lex.return_token()
            while self.token == "commatk":
                self.token = self.lex.return_token()
                if self.token == "idtk":
                    function.add_variable(self.lex.get_id_value())
                    function.set_entity(self.lex.get_id_value())
                    self.writer_to_c.add_variable(self.lex.get_id_value())
                    self.token = self.lex.return_token()
                else:
                    print("Line: " + str(self.lex.get_line()) +
                            "\nSyntax Error: Expected id after comma\n")

    def subprograms(self):
        while self.token == "functiontk" or self.token == "proceduretk":
            self.token = self.lex.return_token()
            self.subprogram()

    def subprogram(self):
        if self.token == "idtk":
            function = self.get_function(self.function_name_for_table)
            function.add_function(self.function_name_for_table)
            name = self.lex.get_id_value()
            self.functions_name.append(name)
            self.function_name_for_table = name
            self.nesting_level += 1
            function = symbol_table(self.nesting_level)
            function.set_parent(self.symbol_table_list[-1].get_function_name())
            function.set_function_name(name)
            self.symbol_table_list.append(function)
            self.token = self.lex.return_token()
            self.funcbody()
            function.set_frame_length()
            function = self.get_function(self.get_function(self.function_name_for_table).\
                                get_parent())
            function.set_entity_function(self.get_function(self.function_name_for_table).\
                            get_function_as_entity())
            self.nesting_level -= 1
            self.functions_name.pop()
            self.function_name_for_table = self.get_function(self.function_name_for_table).get_parent()
            self.semi_code.gen_quad("end_block", name, "_", "_")
            self.semi_code.next_quad()
        else:
            print("Line: " + str(self.lex.get_line()) +
                        " Expected id for subprogram\n")
            sys.exit()

    def funcbody(self):
        self.formalpars()
        if self.token == "left_curly_brackettk":
            self.token = self.lex.return_token()
            self.block()
            if self.token == "right_curly_brackettk":
                self.token = self.lex.return_token()
            else:
                print("Line: " + str(self.lex.get_line()) +
                        "\nSyntax Error: Expected '}' after block\n")
                sys.exit()
        else:
            print("Line: " + str(self.lex.get_line()) +
                        "\nSyntax Error: Expected '{' after block\n")
            sys.exit()

    def formalpars(self):
        if self.token == "left_round_brackettk":
            self.token = self.lex.return_token()
            self.formalparlist()
            if self.token == "right_round_brackettk":
                self.token = self.lex.return_token()
            else:
                print("Line: " + str(self.lex.get_line()) +
                        "\nSyntax Error: Expected ')' after formalparlist\n")
                sys.exit()
        else:
            print("Line: " + str(self.lex.get_line()) +
                    "\nSyntax Error: Expected '(' before formalparlist\n")
            sys.exit()

    def formalparlist(self):
        self.formalparitem()
        while self.token == "commatk":
            self.token = self.lex.return_token()
            self.formalparitem()

    def formalparitem(self):
        function = self.get_function(self.function_name_for_table)
        if self.token == "intk":
            function.add_par_type("in")
            self.token = self.lex.return_token()
            if self.token == "idtk":
                function.add_variable(self.lex.get_id_value())
                function.set_entity(self.lex.get_id_value())
                self.token = self.lex.return_token()
            else:
                print("Line: " + str(self.lex.get_line()) +
                            " Expected id after in\n")
        elif self.token == "inouttk":
            function.add_par_type("io")
            self.token = self.lex.return_token()
            if self.token == "idtk":
                function.add_variable(self.lex.get_id_value())
                function.set_entity(self.lex.get_id_value())
                self.token = self.lex.return_token()
            else:
                print("Line: " + str(self.lex.get_line()) +
                            " Expected id after inout\n")
                sys.exit()

    def statements(self):
        self.statement()
        if self.token == "left_curly_brackettk":
            self.token = self.lex.return_token()
            self.statement()
            while self.token == "questiontk":
                self.token = self.lex.return_token()
                self.statement()
            if self.token == "right_curly_brackettk":
                self.token = self.lex.return_token()
            else:
                print("Line: " + str(self.lex.get_line()) +
                        "\nSyntax Error: Expected '}' after statement\n")
                sys.exit()

    def statement(self):
        if self.token == "idtk":
            self.left = self.lex.get_id_value()
            self.token = self.lex.return_token()
            self.assignment_stat()
        elif self.token == "iftk":
            self.token = self.lex.return_token()
            self.if_stat()
        elif self.token == "whiletk":
            self.token = self.lex.return_token()
            self.while_stat()
        elif self.token == "doublewhiletk":
            self.token = self.lex.return_token()
            self.doublewhile_stat()
        elif self.token == "looptk":
            self.token = self.lex.return_token()
            self.loop_stat()
        elif self.token == "exittk":
            self.token = self.lex.return_token()
        elif self.token == "forcasetk":
            self.token = self.lex.return_token()
            self.forcase_stat()
        elif self.token == "incasetk":
            self.token = self.lex.return_token()
            self.incase_stat()
        elif self.token == "returntk":
            self.token = self.lex.return_token()
            self.return_stat()
        elif self.token == "calltk":
            self.token = self.lex.return_token()
            self.call_stat()
        elif self.token == "printtk":
            self.token = self.lex.return_token()
            self.print_stat()
        elif self.token == "inputtk":
            self.token = self.lex.return_token()
            self.input_stat()
        # else:
        #     print("Line: " + str(self.lex.get_line()) +
        #             " Statements expected at least one statement\n")
        #     sys.exit()

    def assignment_stat(self):
        if self.token == "assignmenttk":
            self.rel = self.lex.get_id_value()
            self.token = self.lex.return_token()
            self.expression()
            self.op.create_quads(self.semi_code, self.op.get_values(),\
                            self.get_function(self.function_name_for_table))
            self.semi_code.gen_quad(self.rel, self.op.get_last(), "_", self.left)
            self.op.clear_values()
        else:
            print("Line: " + str(self.lex.get_line()) +
                    " Expected id assignment\n")
            sys.exit()

    def if_stat(self):
        if self.token == "left_round_brackettk":
            self.token = self.lex.return_token()
            self.semi_code.set_b_quad(self.semi_code.get_label())
            self.condition()
            if self.token == "right_round_brackettk":
                self.token = self.lex.return_token()
                if self.token == "thentk":
                    self.token = self.lex.return_token()
                    self.semi_code.gen_quad("jump", "_", "_", "_")
                    self.semi_code.next_quad()
                    self.semi_code.back_path(self.semi_code.get_label(), "not_jump")
                    self.statements()
                    self.semi_code.back_path(self.semi_code.get_label(), "jump")
                    self.elsepart()
                else:
                    print("Line: " + str(self.lex.get_line()) +
                            "\nSyntax Error: Expected then after ')'\n")
                    sys.exit()
            else:
                print("Line: " + str(self.lex.get_line()) +
                            "\nSyntax Error: Expected ')' after condition\n")
                sys.exit()
        else:
            print("Line: " + str(self.lex.get_line()) +
                    "\nSyntax Error: Expected '(' after if\n")
            sys.exit()

    def elsepart(self):
        if self.token == "elsetk":
            self.token = self.lex.return_token()
            self.statements()


    def while_stat(self):
        if self.token == "left_round_brackettk":
            self.token = self.lex.return_token()
            self.semi_code.set_b_quad(self.semi_code.get_label())
            self.condition()
            self.semi_code.gen_quad("jump", "_", "_", "_")
            self.semi_code.next_quad()
            if self.token == "right_round_brackettk":
                self.semi_code.back_path(self.semi_code.get_label(), "not_jump")
                self.token = self.lex.return_token()
                self.statements()
                self.semi_code.gen_quad("jump", "_", "_", self.semi_code.get_b_quad())
                self.semi_code.next_quad()
                self.semi_code.back_path(self.semi_code.get_label(), "jump")
            else:
                print("Line: " + str(self.lex.get_line()) +
                        "\nSyntax Error: Expected ')' after condition\n")
                sys.exit()
        else:
            print("Line: " + str(self.lex.get_line()) +
                    "\nSyntax Error: Expected '(' after while\n")
            sys.exit()

    def doublewhile_stat(self):
        self.while_stat()
        if self.token == "elsetk":
            self.token = self.lex.return_token()
            self.statements()
        else:
            print("Line: " + str(self.lex.get_line()) +
                    " Expected else for doublewhile\n")
            sys.exit()

    def loop_stat(self):
        self.statements()

    def forcase_stat(self):
        self.semi_code.set_b_quad(self.semi_code.get_label())
        self.when_stat()
        if self.token == "defaulttk":
            self.token = self.lex.return_token()
            if self.token == "colontk":
                self.token = self.lex.return_token()
                self.statements()
            else:
                print("Line: " + str(self.lex.get_line()) +
                        "\nSyntax Error: Expected ':' after default\n")
                sys.exit()
        else:
            print("Line: " + str(self.lex.get_line()) +
                    " Expected default for forcase\n")
            sys.exit()

    def when_stat(self):
        while self.token == "whentk":
            self.token = self.lex.return_token()
            if self.token == "left_round_brackettk":
                self.token = self.lex.return_token()
                self.condition()
                if self.token == "right_round_brackettk":
                    self.token = self.lex.return_token()
                    if self.token == "colontk":
                        self.token = self.lex.return_token()
                        self.semi_code.gen_quad("jump", "_", "_", "_")
                        self.semi_code.next_quad()
                        self.semi_code.back_path(self.semi_code.get_label(), "not_jump")
                        self.statements()
                        self.semi_code.back_path(self.semi_code.get_label(), "jump")
                    else:
                        print("Line: " + str(self.lex.get_line()) +
                            "\nSyntax Error: Expected ':' after condition\n")
                        sys.exit()
                else:
                    print("Line: " + str(self.lex.get_line()) +
                            "\nSyntax Error: Expected ')' for condition\n")
                    sys.exit()
            else:
                print("Line: " + str(self.lex.get_line()) +
                        "\nSyntax Error: Expected '(' after when\n")
                sys.exit()

    def incase_stat(self):
        self.when_stat()

    def return_stat(self):
        self.expression()
        self.op.create_quads(self.semi_code, self.op.get_values(),\
                self.get_function(self.function_name_for_table))
        self.semi_code.gen_quad("retv", self.op.get_last(), "_", "_")
        self.semi_code.next_quad()
        self.op.clear_values()

    def call_stat(self):
        if self.token == "idtk":
            name = self.lex.get_id_value()
            self.token = self.lex.return_token()
            self.op.clear_values()
            if self.token == "left_round_brackettk":
                self.token = self.lex.return_token()
                self.actualpars()
                self.semi_code.gen_quad("call", name, "_", "_")
                self.semi_code.next_quad()
            else:
                print("Line: " + str(self.lex.get_line()) +
                            "\nSyntax Error: Expected '(' before in or inout\n")
                sys.exit()
        else:
            print("Line: " + str(self.lex.get_line()) +
                        " Expected id for call\n")
            sys.exit()

    def print_stat(self):
        if self.token == "left_round_brackettk":
            self.op.clear_values()
            self.token = self.lex.return_token()
            self.expression()
            self.op.create_quads(self.semi_code, self.op.get_values(),\
                        self.get_function(self.function_name_for_table))
            self.semi_code.gen_quad("out", self.op.get_last(), "_", "_")
            self.semi_code.next_quad()
            if self.token == "right_round_brackettk":
                self.token = self.lex.return_token()
            else:
                print("Line: " + str(self.lex.get_line()) +
                        "\nSyntax Error: Expected ')' after expression\n")
                sys.exit()
        else:
            print("Line: " + str(self.lex.get_line()) +
                    "\nSyntax Error: Expected '(' after print\n")
            sys.exit()

    def input_stat(self):
        if self.token == "left_round_brackettk":
            self.token = self.lex.return_token()
            if self.token == "idtk":
                self.semi_code.gen_quad("inp", self.lex.get_id_value(), "_", "_")
                self.semi_code.next_quad()
                self.token = self.lex.return_token()
                if self.token == "right_round_brackettk":
                    self.token = self.lex.return_token()
                else:
                    print("Line: " + str(self.lex.get_line()) +
                            "\nSyntax Error: Expected ')' after id\n")
                    sys.exit()
            else:
                print("Line: " + str(self.lex.get_line()) +
                        " Expected id for input\n")
                sys.exit()
        else:
            print("Line: " + str(self.lex.get_line()) +
                    "\nSyntax Error: Expected '(' after input\n")
            sys.exit()

    def actualpars(self):
        self.actualparlist()
        if self.token == "right_round_brackettk":
            self.token = self.lex.return_token()
        else:
            print("Line: " + str(self.lex.get_line()) +
                    "\nSyntax Error: Expected ')' after expression or id\n")
            sys.exit()

    def actualparlist(self):
        self.actualparitem()
        while self.token == "commatk":
            self.token = self.lex.return_token()
            self.actualparitem()

    def actualparitem(self):
        if self.token == "intk":
            self.token = self.lex.return_token()
            self.op.clear_values()
            self.expression()
            self.op.create_quads(self.semi_code, self.op.get_values(),\
                        self.get_function(self.function_name_for_table))
            self.semi_code.gen_quad("par", "_", self.op.get_last() ,"CV")
            self.semi_code.next_quad()
            self.op.clear_values()
        elif self.token == "inouttk":
            self.token = self.lex.return_token()
            if self.token == "idtk":
                self.semi_code.gen_quad("par", "_",
                        self.lex.get_id_value(), "REF")
                self.semi_code.next_quad()
                self.token = self.lex.return_token()
            else:
                print("Line: " + str(self.lex.get_line()) +
                        " Expected id after inout\n")
                sys.exit()

    def condition(self):
        self.boolterm()
        while self.token == "ortk":
            self.logical = "or"
            self.token = self.lex.return_token()
            self.boolterm()
        self.not_boolean = False

    def boolterm(self):
        self.boolfactor()
        while self.token == "andtk":
            self.logical = "and"        #αν ειναι αληθης η and πηγαινει απο κατω στο backpatch
            #self.semi_code.gen_quad("jump", "_", "_", "_")                       #an einai ψευδης η and
            self.semi_code.gen_quad("jump", "_", "_", "_")
            self.semi_code.next_quad()
            self.token = self.lex.return_token()
            self.semi_code.back_path(self.semi_code.get_label(), "not_jump")  #
            self.boolfactor()

    def boolfactor(self):
        if self.token == "nottk":
            self.not_boolean = True
            self.token = self.lex.return_token()
            if self.token == "left_square_brackettk":
                self.token = self.lex.return_token()
                self.condition()
                if self.token == "right_square_brackettk":
                    self.token = self.lex.return_token()
                else:
                    print("Line: " + str(self.lex.get_line()) +
                            "\nSyntax Error: Expected ']' after condition\n")
                    sys.exit()
            else:
                print("Line: " + str(self.lex.get_line()) +
                        "\nSyntax Error: Expected '[' before condition\n")
                sys.exit()
        elif self.token == "left_square_brackettk":
            self.token = self.lex.return_token()
            self.condition()
            if self.token == "right_square_brackettk":
                self.token = self.lex.return_token()
            else:
                print("Line: " + str(self.lex.get_line()) +
                        "\nSyntax Error: Expected ']' after condition\n")
                sys.exit()
        else:
            self.expression()
            self.op.create_quads(self.semi_code, self.op.get_values(),\
                            self.get_function(self.function_name_for_table))
            self.left = self.op.get_last()
            self.rel = self.lex.get_id_value()
            self.relational_oper()
            self.op.clear_values()
            self.expression()
            self.op.create_quads(self.semi_code, self.op.get_values(),\
                            self.get_function(self.function_name_for_table))
            if self.not_boolean == True:
                if self.rel == ">":
                    self.semi_code.gen_quad("<=", self.left, self.op.get_last(), "_")
                elif self.rel == "<":
                    self.semi_code.gen_quad(">=", self.left, self.op.get_last(), "_")
                elif self.rel == "=":
                    self.semi_code.gen_quad("<>", self.left, self.op.get_last(), "_")
                elif self.rel == "<>":
                    self.semi_code.gen_quad("=", self.left, self.op.get_last(), "_")
                elif self.rel == ">=":
                    self.semi_code.gen_quad("<", self.left, self.op.get_last(), "_")
                elif self.rel == "<=":
                    self.semi_code.gen_quad(">", self.left, self.op.get_last(), "_")
            else:
                self.semi_code.gen_quad(self.rel, self.left, self.op.get_last(), "_")
            self.semi_code.next_quad()
            self.op.clear_values()

    def expression(self):
        self.optional_sign()
        self.term()
        while self.token == "plustk" or self.token == "minustk":
            self.op.add(self.lex.get_id_value())
            self.token = self.lex.return_token()
            self.term()

    def optional_sign(self):
        self.add_oper()

    def term(self):
        self.op.add(self.lex.get_id_value())
        self.factor()
        while self.token == "multiplytk" or self.token == "dividetk":
            self.op.add(self.lex.get_id_value())
            self.token = self.lex.return_token()
            self.op.add(self.lex.get_id_value())
            self.factor()

    def factor(self):
        if self.token == "constanttk":
            self.token = self.lex.return_token()
        elif self.token == "left_round_brackettk":
            self.token = self.lex.return_token()
            self.expression()
            if self.token == "right_round_brackettk":
                self.op.add(self.lex.get_id_value())
                self.token = self.lex.return_token()
            else:
                print("Line: " + str(self.lex.get_line()) +
                        "\nSyntax Error: Expected ')' after expression\n")
                sys.exit()
        elif self.token == "idtk":
            if self.function_open == 0:
                self.function_call = self.lex.get_id_value()
            self.token = self.lex.return_token()
            self.idtail()
            if self.function_open == 1:
                self.function_open = 0
        else:
            print("Line: " + str(self.lex.get_line()) +
                    "\nError factor can't be null\n")
            sys.exit()

    def idtail(self):
        if self.token == "left_round_brackettk":
            self.function_open = 1
            self.token = self.lex.return_token()
            self.op.clear_values()
            self.actualpars()
            self.semi_code.gen_quad("par", "_", self.semi_code.new_temp(), "RET")
            self.semi_code.next_quad()
            self.semi_code.gen_quad("call", self.function_call, "_", "_")
            self.semi_code.next_quad()
            self.op.set_last(self.semi_code.get_temp())
            self.op.clear_values()

    def relational_oper(self):
        if self.token == "equaltk":
            self.token = self.lex.return_token()
        elif self.token == "lessequaltk":
            self.token = self.lex.return_token()
        elif self.token == "greaterequaltk":
            self.token = self.lex.return_token()
        elif self.token == "lesstk":
            self.token = self.lex.return_token()
        elif self.token == "greatertk":
            self.token = self.lex.return_token()
        elif self.token == "notequaltk":
            self.token = self.lex.return_token()
        else:
            print("Line: " + str(self.lex.get_line()) +
                    "\nSyntax Error: Expected relational oper\n")
            sys.exit()

    def add_oper(self):
        if self.token == "plustk":
            self.op.add(self.lex.get_id_value())
            self.token = self.lex.return_token()
        elif self.token == "minustk":
            self.op.add(self.lex.get_id_value())
            self.token = self.lex.return_token()

class semi_code():

    def __init__(self):
        self.all_quads = []     #Gia oles tis 4ades
        self.quad = ["_" for i in range(0, 4)]  #Gia 1 4ada
        self.label = 0
        self.temp = -1
        self.b_quad = 0         #Gia ton arithmo tou label prin thn sunthhkh
        self.function = None

    def get_all_quads(self):
        return self.all_quads

    def get_label(self):
        return self.label

    def get_b_quad(self):
        return self.b_quad;

    def next_quad(self):
        self.label += 1
        return self.label

    def gen_quad(self, op, x, y, z):
        self.quad[0], self.quad[1], self.quad[2], self.quad[3] = op, x, y, z
        self.all_quads.append(self.quad)
        self.empty_list()

    def new_temp(self):
        self.temp += 1
        self.function.add_variable("T_" + str(self.temp))
        self.function.set_entity("T_" + str(self.temp))
        return "T_" + str(self.temp)

    def get_temp(self):
        return "T_" + str(self.temp)

    def get_temp_var(self):
        return self.temp

    def empty_list(self):
        self.quad = ["_" for i in range(0, 4)]

    def set_b_quad(self, b_quad):
        self.b_quad = b_quad

    def back_path(self, z, jump_or_not):
        for i in range(self.b_quad, self.get_all_quad_size()):
            if (jump_or_not == "not_jump"):
                if (self.all_quads[i][1] != "_" and self.all_quads[i][2] != "_"):
                    if (self.all_quads[i][0] != "jump"):
                        if (self.all_quads[i][3] == "_"):
                            self.all_quads[i][3] = z
            elif (jump_or_not == "jump"):
                if (self.all_quads[i][0] == "jump" and self.all_quads[i][3] == "_"):
                    self.all_quads[i][3] = z

    def get_all_quad_size(self):
        return len(self.all_quads)

    def set_function(self, function):
        self.function = function

    def print_all_quads(self, writer):
        for i in range(0, self.get_all_quad_size()):
            writer.write_to_file(str(i+1) + " : ")
            for j in range(0, len(self.all_quads[i])):
                writer.write_to_file(str(self.all_quads[i][j]) + " ")
            writer.write_to_file('\n')
        writer.close_writer()

class operation(): #krataei tis pra3eis ta +,-klp

    def __init__(self):
        self.values = []    #gia oles tis times(metavlhtes - arithmous)
        self.last = ""      #O teleutaios xarakthras(T_0 h metavlhth)
        self.last_rel = ""  #To teleutaio relational oper

    def get_values(self):
        return self.values

    def get_last(self):
        return self.last

    def set_last(self, last):
        self.last = last

    def add(self, x):
        self.values.append(x)

    def get_last_value(self):
        if len(self.values) >= 1:
            return self.values[len(self.values) - 1]

    def create_quads(self, semi_code, values, function):
        semi_code.set_function(function)
        last = ""       #Gia thn anadromh
        i = 0           #counter
        while i < len(values):
            if values[i].isalpha() or values[i].isdigit():
                self.last = values[i]
                last = values[i]
            if values[i] == "(":    #a + (a + b)
                nested = []         #lista san to values alla gia na nested (auta mesa sti parenthesdi)
                i += 1              #Diavasame to '(' opote den to theloume allo
                while i < len(values) and values[i] != ")":
                    nested.append(values[i])
                    i += 1
                nested_last = self.create_quads(semi_code, nested, function)
                semi_code.gen_quad(self.last_rel, last, nested_last,
                                    semi_code.new_temp())
                semi_code.next_quad()
                last = semi_code.get_temp()
                self.last = semi_code.get_temp()
            elif values[i] == "+" or "-" or "*" or "/":
                if i >= 1 and i <= len(values) - 2:
                    if values[i + 1] != "(":
                        semi_code.gen_quad(values[i], values[i - 1],
                                    values[i + 1], semi_code.new_temp())
                        semi_code.next_quad()
                        last = semi_code.get_temp()
                        self.last = semi_code.get_temp()
                        i += 1
                    elif values[i + 1] == "(":  #a + (b + a)
                        self.last_rel = values[i]
            i += 1
        return last

    def print_values(self):
        print(self.values)

    def clear_values(self):
        self.values = []

class symbol_table():

    def __init__(self, nesting_level):
        self.nesting_level = nesting_level
        self.offset = 12
        self.entities = []
        self.pars_type = []
        self.variables = []
        self.functions = []
        self.parent = ""
        self.var_w_offset = {}

    def add_var_w_offset(self, key, value):
        self.var_w_offset[key] = value

    def get_var_w_offset(self):
        return self.var_w_offset

    def get_x_in_var_w_offset(self, x):
        return self.var_w_offset.get(str(x))

    def get_nesting_level(self):
        return self.nesting_level

    def set_parent(self, x):
        self.parent = x

    def get_parent(self):
        return self.parent

    def get_offset(self):
        return self.offset

    def increase_offset(self):
        self.offset += 4

    def set_frame_length(self):
        self.frame_length = self.offset

    def add_variable(self, x):
        self.variables.append(x)

    def get_variables(self):
        return self.variables

    def add_function(self, x):
        self.functions.append(x)

    def get_functions(self):
        return self.functions

    def set_function_name(self, name):
        self.function_name = name

    def get_function_name(self):
        return self.function_name

    def add_par_type(self, x):
        self.pars_type.append(x)

    def get_pars_type_as_list(self):
        return self.pars_type

    def get_pars_type(self):
        pars_string = ""
        count = 0
        for pars in self.pars_type:
            if count == 0:
                pars_string += str(pars)
            else:
                pars_string += ", " + str(pars)
            count += 1
        return pars_string

    def get_function_as_entity(self):
        return self.function_name + ", "  + self.get_pars_type() + ", "\
                        + str(self.frame_length)

    def set_entity(self, x):
        self.add_var_w_offset(str(self.get_offset), x)
        entity = str(x) + " : " + str(self.get_offset())
        self.increase_offset()
        self.entities.append(entity)

    def set_entity_function(self, x):
        entity = str(x)
        self.entities.append(entity)

    def print_function(self):
        count = 0
        entities = ""
        for entity in self.entities:
            if count == 0:
                entities += str(entity)
            else:
                entities += str(", ") + str(entity)
            count += 1
        print("\n----" + str(self.function_name) + "----\n")
        print("Father: " + str(self.parent))
        print("Level: " + str(self.nesting_level))
        print(entities)

class semi_code_output_file():

    def __init__(self):
        self.writer = open("semi_code.int", "w")

    def write_to_file(self, line):
        self.writer.write(str(line))

    def close_writer(self):
        self.writer.close()

class semi_code_c_file():

    def __init__(self):
        self.variables = []
        self.writer = open("semi_code.c", "w")

    def write_main(self):
        self.writer.write("int main()\n{\n")

    def close_main(self):
        self.writer.write("}\n")

    def add_variable(self, x):
        self.variables.append(x)

    def write_variables(self):
        self.writer.write("\tint ")
        if (len(self.variables) >= 1):
            self.writer.write(str(self.variables[0]))
            for i in range(1, len(self.variables)):
                self.writer.write(", " + str(self.variables[i]))
        self.writer.write(";\n\tL_1:\n")

    def fill_c_file(self, all_quads):
        self.write_main()
        self.write_variables()
        counter = 2
        for i in range(0, len(all_quads)):
            if all_quads[i][0] == ">" or all_quads[i][0] == ">="\
                    or all_quads[i][0] == "<" or all_quads[i][0] == "<="\
                    or all_quads[i][0] == "=" or all_quads[i][0] == "<>":
                self.writer.write("\tL_" + str(counter) + ": " +\
                            str(all_quads[i][1]) + str(all_quads[i][0]) +\
                            str(all_quads[i][2]) +\
                            " goto L_" + str(all_quads[i][3]) + ";\n")
                counter += 1
            if all_quads[i][0] == ":=":
                self.writer.write("\tL_" + str(counter) + ": " +\
                    str(all_quads[i][3]) + str(all_quads[i][0]) +\
                    str(all_quads[i][1]) + ";\n")
                counter += 1
            if all_quads[i][0] == "jump":
                self.writer.write("\tL_" + str(counter) + ": goto L_" +\
                    str(all_quads[i][3]) + ";\n")
            if all_quads[i][0] == "+" or all_quads[i][0] == "-"\
                    or all_quads[i][0] == "*" or all_quads[i][0] == "/":
                self.writer.write("\tL_" + str(counter) + ": " +\
                            str(all_quads[i][3]) + " = "  + str(all_quads[i][1])\
                            + str(all_quads[i][0]) + str(all_quads[i][2]) + ";\n")
                counter += 1
            if all_quads[i][0] == "out":
                self.writer.write("\tL_" + str(counter) + ": print(" +\
                    str(all_quads[i][1]) + ");\n")
                counter += 1
        self.writer.write("\tL_" + str(counter) +":" +" " + "{}\n")
        self.close_main()
        self.close_writer()

    def write_to_file(self, line):
        self.writer.write(str(line))

    def close_writer(self):
        self.writer.close()

class final_code():

    def __init__(self, symbol_table_list):
        self.symbol_table_list = symbol_table_list
        self.function = None
        self.case = ""
        self.offset = 0

    def write_final_code(self, result):
        f = open("final_code.asm", "w")
        f.write(result)
        f.close()

    def get_offset(self):
        return self.offset

    def set_function_name(self, function_name):
        self.current_function_name = function_name

    def get_t(self):
        self.t
        return self.t

    def gnvlcode(self, v):
        count = 0
        self.offset = self.search_in_function(v)
        result = ""
        while self.offset == -1:
            self.current_function_name = self.function.get_parent()
            if self.current_function_name == "":
                count = -1
                break
            if count == 0:
                result += ("\tlw $t0, -4($sp)\n")
            else:
                result += ("\tlw $t0, -4($t0)\n")
            count += 1
            self.offset = self.search_in_function(v)
        if count == 0:
            result += ("\tlw $t0, -4($sp)\n")
        if count == -1:
            print("Variable with name: " +str(v) + ", hasn't declared...")
            sys.exit()
        else:
            result += ("\taddi $t0, $t0, -" + str(self.offset) + "\n")
        return result

    def loadvr(self, v, r):
        function = self.get_function()
        flag = False
        result = ""
        if v.isdigit():
            self.case = "constant"
            result += ("\tli " + str(r) + "," + str(v) + "\n")
            flag = True
        elif self.is_global(v):
            index = self.symbol_table_list[0].get_variables().index(v)
            self.offset = 12 + index * 4
            result += ("\tlw " + str(r) + ",-" + str(self.offset) + "($s0)\n")
            flag = True
        elif self.is_local(v, function):
            index = function.get_variables().index(v)
            self.offset = 12 + (index) * 4
            if index < len(function.get_pars_type()):
                if self.is_inout(v, function, index):
                    result += ("\tlw $t0, -" + str(self.offset) + "($sp)\n")
                    result += ("\tlw " + str(r) + ", ($t0)\n")
                    flag = True
            else:
                result += ("\tlw " + str(r) + ", -" + str(self.offset) + "($sp)\n")
                flag = True
        if flag == False:
            result += self.gnvlcode(v)
            self.case = "parent"
            if v in self.function.get_variables():
                index = self.function.get_variables().index(v)
                if index < len(self.function.get_pars_type()):
                    self.case = "parent_ref"
                    if self.function.get_pars_type()[index] == "inout":
                        self.offset = 12 + (index) * 4
                        result += ("\tlw $t0, ($t0)\n")
            #print("sw " + str(r) + ", ($t0)")
        return result

    def is_global(self, v):
        if v in self.symbol_table_list[0].get_variables():
            self.case = "global"
            return True
        return False

    def is_local(self, v, function):
        if v in function.get_variables():
            self.case = "local"
            return True
        return False

    def is_inout(self, v, function, index):
        if function.get_pars_type()[index] == "inout":
            self.case = "local_ref"
            return True
        return False

    def storev(self, r, v):
        function = self.get_function()
        result = ""
        if self.case == "global":
            index = self.symbol_table_list[0].get_variables().index(v)
            self.offset = 12 + index * 4
            result += ("\tsw " + str(r) + ", -" + str(self.offset) + "($s0)\n")
        elif self.case == "local" or self.case == "constant":
            index = function.get_variables().index(v)
            self.offset = 12 + (index) * 4
            result += ("\tsw " + str(r) + ",-" + str(self.offset) + "($sp)\n")
        elif self.case == "local_ref":
            index = function.get_variables().index(v)
            self.offset = 12 + (index) * 4
            result += ("\tlw $t0, -" + str(self.offset) + "($sp)\n")
            result += ("\tsw " + str(r) + ",($t0)\n")
        elif self.case == "parent":
            result += self.gnvlcode(v)
            result += ("\tsw " + str(r) + ",($t0)\n")
        elif self.case == "parent_ref":
            result += self.gnvlcode(v)
            result += ("\tlw $t0,($t0)\n")
            result += ("\tsw " + str(r) + ",($t0)\n")
        return result

    def get_function(self):
        for function in self.symbol_table_list:
            if function.get_function_name() == self.current_function_name:
                return function
        print("Can't find function with name: " + str(self.current_function_name))
        sys.exit()

    def get_function_x(self, function_x):
        for function in self.symbol_table_list:
            if function.get_function_name() == function_x:
                return function
        print("Can't find function with name: " + str(self.function_x))
        sys.exit()

    def search_in_function(self, v):
        self.function = self.get_function()
        function_vars = self.function.get_variables()
        for i in range(0, len(function_vars)):
            if function_vars[i] == v:
                return 4 * (i + 3)
        return -1

class read_semi_code():

    def __init__(self, all_quads, symbol_table_list):
        self.all_quads = all_quads
        self.symbol_table_list = symbol_table_list
        self.final_code = final_code(self.symbol_table_list)
        self.label = 0
        self.function_begin = {}

    def write_result(self, result):
        self.final_code.write_final_code(result)

    def read_quads(self):
        pars = []
        result = ""
        result += ("L" + str(self.label) + ":\n\tj Lmain\n")
        self.label += 1
        for quad in self.all_quads:
            if not self.is_main_name(quad[1]) and not quad[0] == "par"\
                and not quad[0] == "call":
                result += ("L" + str(self.label) + ":\n")
            if self.is_begin_block_label(quad[0]):
                self.function_begin[quad[1]] = "L" + str(self.label)
                if self.is_main_name(quad[1]):
                    result += self.write_lmain()
                else:
                    result += ("\tsw $ra, -0($sp)\n")
                self.final_code.set_function_name(quad[1])
            elif self.is_end_block_label(quad[0]):
                if not self.is_main_name(quad[1]):
                    result += ("\tlw $ra, -0($sp)\n")
                    result += ("\tjr $ra\n")
                else:
                    result += ("L" + str(self.label) + ":\n")
            elif self.is_return_label(quad[0]):
                result += self.final_code.loadvr(quad[1], "$t1")
                result += ("\tlw $t1,-8($sp)\n")
                result += ("\tsw $t1,($t0)\n")
            elif self.is_in_label(quad[0]):
                result += ("\tli $v0, 5\n")
                result += ("\tsyscall\n")
                result += self.final_code.storev("$v0", quad[1])
            elif self.is_out_label(quad[0]):
                result += ("\tli $v0, 1\n")
                result += self.final_code.loadvr(quad[1], "$a0")
                result += ("\tsyscall\n")
            elif self.is_relop(quad[0]):
                result += self.final_code.loadvr(quad[1], "$t1")
                result += self.final_code.loadvr(quad[2], "$t2")
                result += ("\t" + str(self.get_relop(quad[0])) +\
                                " $t1, $t2, L" +str(quad[3])  + "\n")
            elif self.is_op(quad[0]):
                result += self.final_code.loadvr(quad[1], "$t1")
                result += self.final_code.loadvr(quad[2], "$t2")
                result += ("\t" + str(self.get_op(quad[0])) + " $t1, $t1, $t2\n")
                result += self.final_code.storev("$t1", quad[3])
            elif self.is_assign_label(quad[0]):
                result += self.final_code.loadvr(quad[1], "$t1")
                result += self.final_code.storev("$t1", quad[3])
            elif self.is_par_label(quad[0]):
                pars.append("L" + str(self.label) + ":")
                function = self.final_code.get_function()
                if self.is_cv(quad[3]):
                    pars.append(self.final_code.loadvr(quad[2], "$t0"))
                    index = function.get_variables().index(quad[2])
                    offset = 12 + 4 * index
                    pars.append("\tsw $t0, -" + str(offset) + "($fp)")
                elif self.is_ref(quad[3]):
                    if quad[2] in function.get_variables():
                        flag, offset = self.find_if_par_is_inout(quad[2],\
                                                                    function)
                        if flag == True:#Anafora idio vathos
                            pars.append("\tlw $t0,-" + str(offset) + "($sp)")
                            pars.append("\tsw $t0,-" + str(offset) + "($fp)")
                        if flag == False:#Topikh h me timh, idio vathos
                            pars.append("\taddi $t0,$sp,-" + str(offset))
                            pars.append("\tsw $t0,-" + str(offset) + "($fp)")
                    else: #allo vathos
                        pars.append(self.final_code.gnvlcode(quad[2]))
                        function = self.final_code.get_function()
                        if quad[2] in function.get_variables():
                            flag, offset = self.find_if_par_is_inout(quad[2],\
                                                                    function)
                            if flag == True:#Anafora allo vathos
                                pars.append("\tlw $t0,($t0)")
                                pars.append("\tsw $t0,-" + str(self.final_code.\
                                                    get_offset()) + "($fp)")
                            if flag == False:#Topikh h me timh, allo vathos
                                pars.append("\tsw $t0,-" + str(self.final_code.\
                                                    get_offset()) + "($fp)")
                else:
                    index = function.get_variables().index(quad[2])
                    offset = 12 + 4 * index
                    pars.append("\taddi $t0, $sp, -" + str(offset))
                    pars.append("\tsw $t0,-8($fp)")
            elif self.is_call_label(quad[0]):
                function = self.final_code.get_function()
                call_function = self.final_code.get_function_x(quad[1])
                count = 0
                for par in pars:
                    result += (str(par) + "\n")
                    if count == 0: result += ("\taddi $fp, $sp, " +\
                                        str(call_function.get_offset()) + "\n")
                    count += 1
                pars = []
                result += ("L" + str(self.label) + ":\n")
                if function.get_nesting_level() == call_function.get_nesting_level():
                    result += ("\tlw $t0,-4($sp)\n")
                    result += ("\tsw $t0,-4($fp)\n")
                else:
                    result += ("\tsw $sp,-4($fp)\n")
                result += ("\taddi $sp, $sp, " + str(call_function.get_offset())\
                                                                        + "\n")
                result += ("\tjal " + self.find_function_label\
                                    (call_function.get_function_name()) + "\n")
                result += ("\taddi $sp, $sp, -" + str(call_function.get_offset())\
                                                                        + "\n")
            elif quad[0] == "jump":
                result += ("\tj L" + str(quad[3]) + "\n")
            self.label += 1
        self.write_result(result)

    def is_main_name(self, function_name):
        if function_name == self.symbol_table_list[0].get_function_name():
            return True
        return False

    def is_begin_block_label(self, x):
        if x == "begin_block":
            return True
        return False

    def is_end_block_label(self, x):
        if x == "end_block":
            return True
        return False

    def is_return_label(self, x):
        if x == "retv":
            return True
        return False

    def is_in_label(self, x):
        if x == "in":
            return True
        return False

    def is_out_label(self, x):
        if x == "out":
            return True
        return False

    def is_assign_label(self, x):
        if x == ":=":
            return True
        return False

    def is_par_label(self, x):
        if x == "par":
            return True
        return False

    def is_call_label(self, x):
        if x == "call":
            return True
        return False

    def is_cv(self, x):
        if x == "CV":
            return True
        return False

    def is_ref(self, x):
        if x == "REF":
            return True
        return False

    def is_relop(self, x):
        if x == ">" or x == ">=" or x == "<" or\
                        x == "<=" or x == "<>" or x == "=":
            return True
        return False

    def get_relop(self, x):
        if x == ">":
            return "bgt"
        elif x == ">=":
            return "bge"
        elif x == "<":
            return "blt"
        elif x == "<=":
            return "ble"
        elif x == "<>":
            return "bne"
        elif x == "=":
            return "beq"
        print("Label: " + str(self.label) + ", not valid relop...")
        sys.exit()

    def is_op(self, x):
        if x == "+" or x == "-" or x == "*" or x == "/":
            return True
        return False

    def get_op(self, x):
        if x == "+":
            return "add"
        elif x == "-":
            return "sub"
        elif x == "*":
            return "mul"
        elif x == "/":
            return "div"
        print("Label: " + str(self.label) + ", not valid op")
        sys.exit()

    def find_function_label(self, x):
        for key, value in self.function_begin.items():
            if key == x:
                return value
        print("Can't find function: " + x)
        sys.exit()

    def find_if_par_is_inout(self, par, function):
        index = function.get_variables().index(par)
        offset = 12 + 4 * index
        if index < len(function.get_pars_type_as_list()):
            if function.get_pars_type_as_list()[index] == "io": #Me anafora
                return True, offset
        return False, offset

    def write_lmain(self):
        result = ("Lmain:\n")
        result += self.write_next_lmain_label()
        return result

    def write_next_lmain_label(self):
        result = ("L" + str(self.label) + ":\n")
        result += ("\taddi $sp, $sp," + str(self.symbol_table_list[0].\
                                                        get_offset()) + "\n")
        result += ("\tmove $s0, $sp\n")
        return result

yac_ob = yac()
input_file = str(sys.argv[1])  #Gia to terminal
#input_file = input("Give a file: ") #Gia ton idle
yac_ob.set_file(input_file)
yac_ob.set_first_token()
yac_ob.program()
