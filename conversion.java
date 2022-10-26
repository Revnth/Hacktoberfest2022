class myStack {
    static final int MAX = 10;
    int top;
    char[] a = new char[MAX];

    myStack() {
        top = -1;
    }

    boolean push(char x) {
        if (top >= (MAX - 1)) {
            System.out.println("Stack Overflow");
            return false;
        } else {
            a[++top] = x;
            return true;
        }
    }

    int pop() {
        if (top < 0) {
            System.out.println("Stack Underflow");
            return Integer.MIN_VALUE;
        } else {
            int x = a[top--];
            return x;
        }
    }

    char peek() {
        if (top < 0) {
            System.out.println("Stack Underflow");
            return 0;
        } else {
            char x = a[top];
            return x;
        }
    }

    int size() {
        return (top + 1);
    }

    boolean isEmpty() {
        return top == -1;
    }

    boolean isFull() {
        return top == MAX - 1;
    }
}

class conversion {
    static boolean checkIfOperand(char ch) {
        return Character.isLetterOrDigit(ch);
    }

    static int precedence(char ch) {
        switch (ch) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            case '^':
                return 3;
        }
        return -1;
    }

    static void covertInfixToPostfix(String expr) {
        int i;
        myStack s = new myStack();
        StringBuilder result = new StringBuilder(new String(""));
        for (i = 0; i < expr.length(); ++i) {
            if (checkIfOperand(expr.charAt(i)))
                result.append(expr.charAt(i));
            else if (expr.charAt(i) == '(' || expr.charAt(i) == '[' || expr.charAt(i) == '{')
                s.push(expr.charAt(i));
            else if (expr.charAt(i) == ')' || expr.charAt(i) == ']' || expr.charAt(i) == '}') {
                if (expr.charAt(i) == ')') {
                    while (!s.isEmpty() && s.peek() != '(') {
                        result.append(s.peek());
                        s.pop();
                    }
                    s.pop();
                }
                if (expr.charAt(i) == ']') {
                    while (!s.isEmpty() && s.peek() != '[') {
                        result.append(s.peek());
                        s.pop();
                    }
                    s.pop();
                }
                if (expr.charAt(i) == '}') {
                    while (!s.isEmpty() && s.peek() != '{') {
                        result.append(s.peek());
                        s.pop();
                    }
                    s.pop();
                }
            } else {
                while (!s.isEmpty() && precedence(expr.charAt(i)) <= precedence(s.peek())) {
                    result.append(s.peek());
                    s.pop();
                }
                s.push(expr.charAt(i));
            }
        }
        while (!s.isEmpty()) {
            result.append(s.peek());
            s.pop();
        }
        System.out.println(result);
    }

    public static void main(String[] args) {
        String expression = "A+B*(C^D-E)";
        covertInfixToPostfix(expression);
    }
}
