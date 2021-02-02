package ch16.q_16_02;

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
 * https://onlinejudge.u-aizu.ac.jp/beta/review.html#RitsCamp18Day3/5191442
 */
public class Main {
    public void exec() {
        int n = stdin.nextInt();
        int m = stdin.nextInt();
        int s = stdin.nextInt() - 1;
        int t = stdin.nextInt() - 1;

        int[] u = new int[m];
        int[] v = new int[m];
        long[] d = new long[m];
        long[] c = new long[m];
        for (int i = 0; i < m; i++) {
            u[i] = stdin.nextInt() - 1;
            v[i] = stdin.nextInt() - 1;
            d[i] = stdin.nextLong();
            c[i] = stdin.nextLong();
        }

        WarshallFloyd wf = new WarshallFloyd(n);
        for (int i = 0; i < m; i++) {
            wf.addEdge(u[i], v[i], d[i]);
        }
        wf.solve();

        FordFulkerson ff = new FordFulkerson(n);
        for (int i = 0; i < m; i++) {
            if (wf.getDist(s, u[i]) + d[i] +wf.getDist(v[i], t) == wf.getDist(s, t)) {
                ff.addEdge(u[i], v[i], c[i]);
            }
        }
        long ans = ff.solve(s, t);
        stdout.println(ans);
    }

    public class WarshallFloyd {
        private int n;
        private long[][] wf;

        public WarshallFloyd(int n) {
            this.n = n;
            this.wf = new long[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++ ) {
                    if (i == j) {
                        this.wf[i][j] = 0;
                    } else {
                        this.wf[i][j] = Long.MAX_VALUE/2-1;
                    }
                }
            }
        }

        public void addEdge(int from, int to, long dist) {
            this.wf[from][to] = dist;
        }

        public void solve() {
            for (int k = 0; k < n; k++) {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        wf[i][j] = Math.min(wf[i][j], wf[i][k] + wf[k][j]);
                    }
                }
            }
        }

        public long getDist(int from, int to) {
            return this.wf[from][to];
        }
    }

    public class FordFulkerson {
        private class Edge {
            private int from;
            private int to;
            private long cost;
            private int rev;
            public Edge(int from, int to, long cost, int rev) {
                this.from = from;
                this.to = to;
                this.cost = cost;
                this.rev = rev;
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
            this.g.get(from).add(new Edge(from, to, cost, toRev));
            this.g.get(to).add(new Edge(to, from, 0, fromRev));
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