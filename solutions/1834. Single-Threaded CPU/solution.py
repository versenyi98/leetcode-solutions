from heapq import heapify, heappop, heappush


class Solution:
    def getOrder(self, tasks):
        availabe_tasks = []
        task_by_enq = {}
        enq_times = set()

        for idx, [enq, processing] in enumerate(tasks):
            if enq not in task_by_enq:
                task_by_enq[enq] = []
            task_by_enq[enq].append((processing, idx))
            enq_times.add(enq)

        enq_times = sorted(list(enq_times))
        current_index = 1

        current_time = enq_times[0]
        available_tasks = task_by_enq[enq_times[0]]
        heapify(available_tasks)
        result = []

        while available_tasks or current_index < len(enq_times):
            while current_index < len(enq_times) and current_time >= enq_times[current_index]:
                for task in task_by_enq[enq_times[current_index]]:
                    heappush(available_tasks, task)
                current_index += 1
            if not available_tasks:
                current_time = enq_times[current_index]
                for task in task_by_enq[enq_times[current_index]]:
                    heappush(available_tasks, task)
                current_index += 1
            proc, idx = heappop(available_tasks)
            result.append(idx)
            current_time += proc
        return result
