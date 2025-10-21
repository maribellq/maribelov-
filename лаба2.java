//мультисписок на Java
import java.util.ArrayList;
import java.util.List;
class Node {
    String value;
    List<Node> children = new ArrayList<>();
    Node(String value) {
        this.value = value;
    }
}
public class Main {
    public static void main(String[] args) {
        Node root = new Node("Root");
        root.children.add(new Node("Child 1"));
        root.children.add(new Node("Child 2"));
        // Отображение
        System.out.println(root.value);
        for (Node child : root.children) {
            System.out.println("  " + child.value);
        }
    }
}

//очередь на Java
import java.util.LinkedList;
import java.util.Queue;
public class Main {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);  // Добавление элемента
        queue.add(2);
        System.out.println(queue.poll());  // Удаление и вывод первого элемента (1)
    }
}

//дек на Java
import java.util.ArrayDeque;
import java.util.Deque;
public class Main {
    public static void main(String[] args) {
        Deque<Integer> deque = new ArrayDeque<>();
        deque.addLast(1);  // Добавление в конец
        deque.addFirst(2); // Добавление в начало
        System.out.println(deque.removeLast());  // Удаление и вывод последнего элемента (1)
    }
}

//приоритетная очередь на Java
import java.util.PriorityQueue;
public class Main {
    public static void main(String[] args) {
        PriorityQueue<Pair> pq = new PriorityQueue<>((a, b) -> Integer.compare(a.priority, b.priority));
        pq.add(new Pair(1, "task 1"));
        pq.add(new Pair(0, "task 2"));
        System.out.println(pq.poll().task);  // Удаление и вывод задачи с наивысшим приоритетом (task 2)
    }
    static class Pair {
        int priority;
        String task;
        Pair(int priority, String task) {
            this.priority = priority;
            this.task = task;
        }
    }
}