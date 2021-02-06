package ch16.q_16_05;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.io.UncheckedIOException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

/**
 * https://atcoder.jp/contests/soundhound2018/submissions/19943084

 */
public class Main {
    public void exec() {
        int h = stdin.nextInt();
        int w = stdin.nextInt();
        char[][] c = new char[h][];
        for (int i = 0; i < h; i++) {
            c[i] = stdin.nextString().toCharArray();
        }

        FordFulkerson ff = new FordFulkerson(h*w+2);
        int[][] diffs = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        long v = 0;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (c[i][j] != '.') {
                    continue;
                }
                v++;
                if ((i+j)%2==0) {
                    ff.addEdge(h*w, i*w+j, 1);
                    for (int[] diff : diffs) {
                        int x = i + diff[0];
                        int y = j + diff[1];
                        if (0 <= x && x < h && 0 <= y && y < w && c[x][y]=='.') {
                            ff.addEdge(i*w+j, x*w+y, 1);
                        }
                    }
                } else {
                    ff.addEdge(i*w+j,h*w+1, 1);
                }
            }
        }

        stdout.println(v - ff.solve(h*w, h*w+1));
    }

    public class FordFulkerson {
        private class Edge {
            private int from;
            private int to;
            private long cost;
            private int rev;
            private boolean origin;
            public Edge(int from, int to, long cost, int rev, boolean origin) {
                this.from = from;
                this.to = to;
                this.cost = cost;
                this.rev = rev;
                this.origin = origin;
            }
        }

        private List<List<Edge>> g;
        private boolean[] seen;

        public FordFulkerson(int n) {
            this.g = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                this.g.add(new ArrayList<>());
            }
            this.seen = new boolean[n];
        }

        public void addEdge(int from, int to, long cost) {
            int fromRev = this.g.get(from).size();
            int toRev = this.g.get(to).size();
            this.g.get(from).add(new Edge(from, to, cost, toRev, true));
            this.g.get(to).add(new Edge(to, from, 0, fromRev, false));
        }

        private void runFlow(Edge e, long f) {
            e.cost -= f;
            this.g.get(e.to).get(e.rev).cost += f;
        }

        private long dfs(int v, int t, long f) {
            if (v==t) return f;

            this.seen[v] = true;
            for (Edge e : this.g.get(v)) {
                if (this.seen[e.to]) continue;
                if (e.cost == 0) continue;

                long flow = this.dfs(e.to, t, Math.min(f, e.cost));
                if (flow==0) continue;

                this.runFlow(e, flow);

                return flow;
            }

            return 0;
        }

        public long solve(int s, int t) {
            long res = 0;
            while (true) {
                Arrays.fill(this.seen, false);
                long flow = this.dfs(s, t, Long.MAX_VALUE);
                if (flow==0) break;
                res += flow;
            }
            return res;
        }
    }


    private static final Stdin stdin = new Stdin(System.in);
    private static final Stdout stdout = new Stdout(System.out);
    private static final Stderr stderr = new Stderr(System.err, true);

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