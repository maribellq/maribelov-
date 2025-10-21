//мультисписок на С++
#include <iostream>
#include <vector>
#include <memory>
class Node {
public:
    std::string value;
    std::vector<std::shared_ptr<Node>> children;
    Node(const std::string& val) : value(val) {}
};
int main() {
    auto root = std::make_shared<Node>("Root");
    root->children.push_back(std::make_shared<Node>("Child 1"));
    root->children.push_back(std::make_shared<Node>("Child 2"));
    // Отображение
    std::cout << root->value << std::endl;
    for (auto& child : root->children) {
        std::cout << "  " << child->value << std::endl;
    }
    return 0;
}

//очередь на С++
#include <iostream>
#include <queue>
int main() {
    std::queue<int> queue;
    queue.push(1);  // Добавление элемента
    queue.push(2);
    std::cout << queue.front() << std::endl;  // Вывод первого элемента (1)
    queue.pop();  // Удаление первого элемента
    return 0;
}

//дек на С++
#include <iostream>
#include <deque>
int main() {
    std::deque<int> deque;
    deque.push_back(1);  // Добавление в конец
    deque.push_front(2); // Добавление в начало
    std::cout << deque.back() << std::endl;  // Вывод последнего элемента (1)
    deque.pop_back();  // Удаление последнего элемента
    return 0;
}

//очередь на С++
#include <iostream>
#include <queue>
int main() {
    std::priority_queue<std::pair<int, std::string>> pq;
    pq.push({1, "task 1"});
    pq.push({0, "task 2"});
    std::cout << pq.top().second << std::endl;  // Вывод задачи с наивысшим приоритетом (task 2)
    pq.pop();  // Удаление элемента с наивысшим приоритетом
    return 0;
}