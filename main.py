import pygame

# Configurações básicas do Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visualização do Heap")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
font = pygame.font.Font(None, 36)

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.up(len(self.heap) - 1)

    def remove(self):
        if len(self.heap) > 1:
            root = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.down(0)
            return root
        elif self.heap:
            return self.heap.pop()
        return None

    def up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def down(self, index):
        last_index = len(self.heap) - 1
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            if left_child <= last_index and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child
            if right_child <= last_index and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def heap_sort(self):
        sorted_heap = self.heap[:]
        n = len(sorted_heap)

        for i in range(n // 2 - 1, -1, -1):
            self._down_copy(sorted_heap, n, i)

        for i in range(n - 1, 0, -1):
            sorted_heap[0], sorted_heap[i] = sorted_heap[i], sorted_heap[0]
            self.display_heap(sorted_heap)  
            pygame.time.delay(500)  
            self._down_copy(sorted_heap, i, 0)

        print("Heap ordenado:", sorted_heap)

    def _down_copy(self, heap, n, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and heap[left] < heap[largest]:
            largest = left
        if right < n and heap[right] < heap[largest]:
            largest = right

        if largest != index:
            heap[index], heap[largest] = heap[largest], heap[index]
            self._down_copy(heap, n, largest)

    def display_heap(self, heap=None):
        if heap is None:
            heap = self.heap
        window.fill(WHITE)
        if heap:
            self._draw_tree(heap, 0, WIDTH // 2, 50, WIDTH // 4)
        pygame.display.flip()

    def _draw_tree(self, heap, index, x, y, x_offset):
        if index < len(heap):
            pygame.draw.circle(window, BLUE, (x, y), 20)
            text = font.render(str(heap[index]), True, WHITE)
            text_rect = text.get_rect(center=(x, y))
            window.blit(text, text_rect)

            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child < len(heap):
                pygame.draw.line(window, BLACK, (x, y), (x - x_offset, y + 80), 2)
                self._draw_tree(heap, left_child, x - x_offset, y + 80, x_offset // 2)

            if right_child < len(heap):
                pygame.draw.line(window, BLACK, (x, y), (x + x_offset, y + 80), 2)
                self._draw_tree(heap, right_child, x + x_offset, y + 80, x_offset // 2)

    def change_priority(self, index, new_value):
        old_value = self.heap[index]
        self.heap[index] = new_value
        if new_value < old_value:
            self.up(index)
        else:
            self.down(index)

    def get_high_priority(self):
        if self.heap:
            return self.heap[0]
        return None


def display_text(text, duration=2000):
    window.fill(WHITE)
    message = font.render(text, True, BLACK)
    text_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(message, text_rect)
    pygame.display.flip()
    pygame.time.delay(duration)

def main():
    heap = BinaryHeap()
    clock = pygame.time.Clock()

    # Conjunto 1: Dados Aleatórios Pequenos
    display_text("Conjunto 1: Dados Aleatórios Pequenos")
    data1 = [10, 5, 20, 1, 15, 30, 25]
    for value in data1:
        heap.insert(value)
        heap.display_heap()
        pygame.time.delay(500)

    # Alterações de Prioridade Conjunto 1
    heap.change_priority(3, 50)
    heap.display_heap()
    pygame.time.delay(500)

    heap.change_priority(1, 8)
    heap.display_heap()
    pygame.time.delay(500)

    # Remoções Conjunto 1
    for _ in range(3):
        heap.remove()
        heap.display_heap()
        pygame.time.delay(500)

    # Heapsort Conjunto 1
    heap.heap_sort()

    # elemento de alta prioridade 
    high_priority = heap.get_high_priority()
    display_text(f"Alta Prioridade: {high_priority}")

    # Conjunto 2: Sequência Crescente
    display_text("Conjunto 2: Sequência Crescente")
    data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for value in data2:
        heap.insert(value)
        heap.display_heap()
        pygame.time.delay(500)

    # Alterações de Prioridade Conjunto 2
    heap.change_priority(4, 15)
    heap.display_heap()
    pygame.time.delay(500)

    heap.change_priority(8, 3)
    heap.display_heap()
    pygame.time.delay(500)

    # Remoções Conjunto 2
    for _ in range(5):
        heap.remove()
        heap.display_heap()
        pygame.time.delay(500)

    # Heapsort Conjunto 2
    heap.heap_sort()

    # elemento de alta prioridade 
    high_priority = heap.get_high_priority()
    display_text(f"Alta Prioridade: {high_priority}")

    # Conjunto 3: Sequência Decrescente
    display_text("Conjunto 3: Sequência Decrescente")
    data3 = [50, 40, 30, 20, 10, 5, 3]
    for value in data3:
        heap.insert(value)
        heap.display_heap()
        pygame.time.delay(500)

    # Alteração de Prioridade Conjunto 3
    heap.change_priority(2, 60)
    heap.display_heap()
    pygame.time.delay(500)

    heap.change_priority(5, 1)
    heap.display_heap()
    pygame.time.delay(500)

    # Remoções Conjunto 3
    for _ in range(3):
        heap.remove()
        heap.display_heap()
        pygame.time.delay(500)

    # Heapsort Conjunto 3
    heap.heap_sort()

    # elemento de alta prioridade 
    high_priority = heap.get_high_priority()
    display_text(f"Alta Prioridade: {high_priority}")

    # Conjunto 4: Dados Aleatórios Maiores
    display_text("Conjunto 4: Dados Aleatórios Maiores")
    data4 = [13, 26, 19, 17, 24, 31, 22, 11, 8, 20, 5, 27, 18]
    for value in data4:
        heap.insert(value)
        heap.display_heap()
        pygame.time.delay(500)

    # Alteração de Prioridade Conjunto 4
    heap.change_priority(7, 35)
    heap.display_heap()
    pygame.time.delay(500)

    heap.change_priority(10, 12)
    heap.display_heap()
    pygame.time.delay(500)

    # Remoções Conjunto 4
    for _ in range(4):
        heap.remove()
        heap.display_heap()
        pygame.time.delay(500)

    # Heapsort Conjunto 4
    heap.heap_sort()

    # elemento de alta prioridade 
    high_priority = heap.get_high_priority()
    display_text(f"Alta Prioridade: {high_priority}")

    pygame.quit()

if __name__ == "__main__":
    main()