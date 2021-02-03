package ch16.q_16_03;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.io.UncheckedIOException;
import java.lang.reflect.Array;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * https://atcoder.jp/contests/jag2014autumn/submissions/19901106
 */
public class Main {
    public void exec() {
        while (true) {
            int n = stdin.nextInt();
            int m = stdin.nextInt();
            int s = stdin.nextInt()-1;
            int t = stdin.nextInt()-1;
            if (n==0&&m==0&&s==-1&&t==-1) break;
            FordFulkerson ff = new FordFulkerson(n);
            for (int i = 0; i < m; i++) {
                int a = stdin.nextInt()-1;
                int b = stdin.nextInt()-1;
                ff.addEdge(a, b, 1);
            }
            ff.solve(s, t);
        }
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

        public void solve(int s, int t) {
            long res = 0;
            while (true) {
                Arrays.fill(this.seen, false);
                long flow = this.dfs(s, t, Long.MAX_VALUE);
                if (flow==0) break;
                res += flow;
            }

            int n = this.g.size();
            List<List<Integer>> g1 = IntStream.range(0, n).mapToObj(unused -> new ArrayList<Integer>()).collect(Collectors.toList());
            List<List<Integer>> g2 = IntStream.range(0, n).mapToObj(unused -> new ArrayList<Integer>()).collect(Collectors.toList());
            for (Edge edge : this.g.stream().flatMap(List::stream).filter(edge -> edge.cost>0).collect(Collectors.toList())) {
                g1.get(edge.from).add(edge.to);
                g2.get(edge.to).add(edge.from);
            }

            Set<Integer> x = this.seek(g1, s);
            Set<Integer> y = this.seek(g2, t);
            int count = 0;
            for (Edge edge : this.g.stream().flatMap(List::stream).filter(edge -> edge.cost>0 && edge.origin).collect(Collectors.toList())) {
                if (x.contains(edge.to) && y.contains(edge.from)) {
                    count++;
                }
            }

            if (count == 0) {
                stdout.println(res, count);
            } else {
                stdout.println(res+1, count);
            }
        }

        private Set<Integer> seek(List<List<Integer>> g, int start) {
            Set<Integer> s = new HashSet<>();
            Deque<Integer> stack = new ArrayDeque<>();
            stack.add(start);
            while (!stack.isEmpty()) {
                int cur = stack.pop();
                s.add(cur);
                for (int nxt : g.get(cur)) {
                    if (!s.contains(nxt)) {
                        stack.add(nxt);
                    }
                }
            }
            return s;
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