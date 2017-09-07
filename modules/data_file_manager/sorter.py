import persistor

class Sorter(Persistor):

    def sort(self):
        if self.p_state:
            self._persisted_sort()
            self.f.close()
        else:
            self._temporary_sort()

    def _persisted_sort(self):
        self._sort_set()

    def _temporary_sort(self):
        f = open(GlobalVariables.DATA_PATH, "r+")
        self._sort_set(f)
        f.close()

    def _sort_set(f=None):
        pass
