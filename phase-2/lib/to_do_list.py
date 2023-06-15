class To_do_list:
    def __init__(self,):
        self.task_list = []

    def add_to_do(self, task):
        if task == "":
            raise Exception("No task added")
        self.task_list.append(task)

    def show_list(self):
        return self.task_list
    
    def completed_task(self, task):
        if task in self.task_list:
            self.task_list.remove(task)
            print(self.task_list)
