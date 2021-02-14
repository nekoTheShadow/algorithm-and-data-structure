package ch05.q_05_08;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.io.UncheckedIOException;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Objects;

/**
 * https://onlinejudge.u-aizu.ac.jp/solutions/problem/2877/review/5222699/neko_the_shadow/JAVA
 */
public class Main {
    public void exec() {
        int n = stdin.nextInt();
        int m = stdin.nextInt();
        double[] a = stdin.nextDoubleArray(n);

        double[][] avg = new double[n+1][n+1];
        for (int i = 0; i <= n; i++) {
            double sum = 0;
            for (int j = i+1; j  <= n; j++) {
                sum += a[j-1];
                avg[i][j] = sum/(j-i);
            }
        }

        double[][] dp = new double[n+1][m+1];
        for (double[] row : dp) {
            Arrays.fill(row, Double.NEGATIVE_INFINITY);
        }
        dp[0][0] = 0;
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                for (int k = 1; k <= m; k++) {
                    dp[i][k] = Math.max(dp[i][k], dp[j][k-1]+avg[j][i]);
                }
            }
        }

        double ans = Arrays.stream(dp[n]).max().getAsDouble();
        stdout.println(ans);
    }

    private static final Stdin stdin = new Stdin(System.in);
    private static final Stdout stdout = new Stdout(System.out);
    private static final Stderr stderr = new Stderr(System.err, false);

    public static void main(String[] args) {
        try {
            new Main().exec();
        } finally {
            stdout.flush();
        }
    }

    // ASCII ONLY
    public static class Stdin {
        private InputStream in;
        private byte[] buf;
        private int ptr;
        private int len;

        public Stdin(InputStream in) {
            this.in = in;
            this.buf = new byte[1024];
            this.ptr = 0;
            this.len = 0;
        }

        public String nextString() {
            StringBuilder sb = new StringBuilder();
            byte b;
            while ((b = read()) != -1) {
                sb.appendCodePoint(b);
            }
            return sb.toString();
        }

        public int nextInt() {
            return (int)nextLong();
        }

        public double nextDouble() {
            return Double.parseDouble(nextString());
        }

        public long nextLong() {
            boolean negative = false;
            int x = 0;

            byte b = read();
            if (b == '-') {
                negative = true;
            } else {
                x += b-'0';
            }

            while ((b=read()) != -1) {
                x *= 10;
                x += b-'0';
            }

            return negative ? -x : x;
        }

        private byte read() {
            byte b = readByte();
            if (b == '\r') {
                readByte(); // LFを読み飛ばす
                return -1;
            } else if (b == '\n' || b == ' ') {
                return -1;
            } else {
                return b;
            }
        }

        private byte readByte(){
            if (len == ptr) {
                try {
                    ptr = 0;
                    len = in.read(buf);
                    if (len == -1) return -1;
                } catch (IOException e) {
                    throw new UncheckedIOException(e);
                }
            }
            return buf[ptr++];
        }

        public String[] nextStringArray(int n) {
            String[] a = new String[n];
            for (int i = 0; i < n; i++) a[i] = nextString();
            return a;
        }

        public int[] nextIntArray(int n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = nextInt();
            return a;
        }

        public double[] nextDoubleArray(int n) {
            double[] a = new double[n];
            for (int i = 0; i < n; i++) a[i] = nextDouble();
            return a;
        }

        public long[] nextLongArray(int n) {
            long[] a = new long[n];
            for (int i = 0; i < n; i++) a[i] = nextLong();
            return a;
        }
    }

    public static class Stdout {
        private PrintWriter stdout;

        public Stdout(PrintStream stdout) {
            this.stdout =  new PrintWriter(stdout, false);
        }

        public void println(Object ... objs) {
            for (int i = 0, len = objs.length; i < len; i++) {
                stdout.print(objs[i]);
                if (i != len-1) stdout.print(' ');
            }
            stdout.println();
        }

        public void flush() {
            stdout.flush();
        }
    }

    public static class Stderr {
        private PrintWriter stderr;
        private boolean debug;

        public Stderr(PrintStream stderr, boolean debug) {
            this.stderr =  new PrintWriter(stderr, false);
            this.debug = debug;
        }

        public void println(Object ... objs) {
            if (!debug) return ;

            stderr.print("DEBUG: ");
            for (int i = 0, len = objs.length; i < len; i++) {
                stderr.print(deepToString(objs[i]));
                if (i != len-1) stderr.print(' ');
            }
            stderr.println();
            stderr.flush();
        }

        private String deepToString(Object o) {
            if (o == null) {
                return "null";
            }

            // 配列の場合
            if (o.getClass().isArray()) {
                int len = Array.getLength(o);
                String[] tokens = new String[len];
                for (int i = 0; i < len; i++) {
                    tokens[i] = deepToString(Array.get(o, i));
                }
                return "{" + String.join(", ", tokens) + "}";
            }

            return Objects.toString(o);
        }
    }
}