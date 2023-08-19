import sys

def guess_arity(code):
    if code == '':
        return 1

    start = code.find(']')
    if start == -1:
        start = len(code)

    while start > 0 and code[start-1] != '[':
        start -= 1

    arity = ''
    while code[start].isdigit():
        arity += code[start]
        start += 1

    if arity == '':
        arity = '1'

    x = int(arity)
    x += code.count('P')
    x -= code.count('M')

    return x

def run_mu(code, stack):
    f_stack = []
    pc = 0
    while pc < len(code):
        if code[pc].isdigit():
            x = code[pc]
            pc += 1
            while code[pc].isdigit():
                x += code[pc]
                pc += 1
            stack.append(int(x))
            pc -= 1 # auto pc += 1 at end

        elif code[pc] == '[':
            seek = pc + 1
            level = 1
            while level > 0:
                level += code[seek] == '['
                level -= code[seek] == ']'
                seek += 1
            f_stack.append(code[pc+1:seek-1])
            pc = seek - 1 # auto pc += 1 at end

        elif code[pc] == 'P':
            g, h = f_stack[0], f_stack[1]
            print(guess_arity(g))
            exit(0)

        elif code[pc] == 'z':
            stack[-1] = 0
        elif code[pc] == 's':
            stack[-1] += 1
        elif code[pc] == 'k':
            i, k = stack.pop(), stack.pop()
            tmp, stack = stack[-k:], stack[:-k]
            stack.append(tmp[i-1])
        pc += 1

    return stack

if __name__ == '__main__':
    code = open(sys.argv[1]).read()
    print(run_mu(code, []))
