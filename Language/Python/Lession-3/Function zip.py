# Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора
# zip([1, 2, 3], [‘о‘, ‘д‘, ‘т‘], [‘f’, ’s’, ’t’])
# ↓
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]
# Нельзя пройтись дважды

users = ['user1', 'user2', 'user3', 'user4', 'user5']                   # Есть некоторый набор данных условных users
ids = [4, 5, 9, 14, 7]                                                  # И некоторый набор данных идификаторов

data = list(zip(users, ids))                                            # в качестве первого аргумента передаем users в качестве
                                                                        # второго ids (users, ids). Можем положить результат куда не
                                                                        # будь например data, что бы не было проблем превращяем в
                                                                        # список list

salary = [111,222,3333]                                                 # Если появиться новый набор данных который требуется
                                                                        # подмешать к исходным пусть это будет salary
data = list(zip(users, ids, salary))                                    # То у нас береться первые элементы из первого набора первые
                                                                        # три элемента из второго набора и весь третий набор мы
                                                                        # получаем список состояший из трех кортежей
print(data)