func = int(input("Введите номер решаемого задания: "))

# Данная программа реализует алгоритм Кнута-Морриса-Пратта для поиска подстроки в строке
# Алгоритм использует префикс-функцию для определения максимальной длины суффикса подстроки, 
# совпадающего с ее префиксом. В данной программе строка 'лилила' задается переменной t, 
# а затем создается список p длины строки t, заполненный нулями. Затем происходит итерация по строке t, 
# и если символы t[j] и t[i] совпадают, то значение p[i] устанавливается равным j+1, 
# иначе, если j=0, то p[i] устанавливается равным 0, иначе j устанавливается равным p[j-1]. 
# В конце программа выводит список p.

if func == 1:
    t = 'лопата'
    p = [0]*len(t)
    j = 0
    i = 1

    while i < len(t):
        if t[j] == t[i]:
            p[i] = j+1
            i += 1
            j += 1
        elif j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]
    
    print(p)

    a = "лилилопаталилилу"
    m = len(t)
    n = len(a)
    i = 0
    j = 0
    while i < n:
        if a[i] == t[j]:
            i += 1
            j += 1
        if j == m:
            print("образ найден")
            break
        elif j > 0:
            j = p[j-1]
        else:
            i += 1
        if i == n and j != m:
            print("образ не найден")

if func == 2:
    def kmp(P, T):
        pl = len(P)
        tl = len(T)
        p = prefixFunction(P + "#" + T)
        count = 0
        for i in range(tl):
            if p[pl + i + 1] == pl:
                count += 1
                print(i - pl)
            # Проверка на совпадение символов
            # Если символы не совпадают, обновляем значение j
            elif i + 1 - pl > 0:
                j = p[pl + i - 1]
        return count

    def prefixFunction(P):
        pl = len(P)
        p = [0] * pl
        j = 0
        for i in range(1, pl):
            while j > 0 and P[i] != P[j]:
                j = p[j - 1]
            if P[i] == P[j]:
                j += 1
            p[i] = j
        return p
    
    print(kmp('лопата', 'лилулопаталилу'))

# Алгоритм Бойера-Мура-Хорспула (БМХ) - это алгоритм поиска подстроки в строке, 
# который использует два различных правила для определения смещения при несовпадении символов. 
# Первое правило - правило плохого символа - определяет смещение на основе последнего вхождения 
# несовпадающего символа в образце. Второе правило - правило хорошего суффикса - определяет 
# смещение на основе наибольшего суффикса образца, совпадающего с префиксом несовпадающего суффикса. 
# Алгоритм БМХ работает быстрее, чем алгоритм КМП, особенно на длинных строках и образцах. 
# Для использования алгоритма БМХ необходимо создать таблицы смещений для каждого символа 
# в образце и для каждого суффикса образца. Затем производится поиск образца в строке, 
# используя правила плохого символа и хорошего суффикса для определения смещения
    
# Алгоритм Бойера-Мура-Хорспула (АБМХ) выводит информацию о начале каждого вхождения образца в строке. 
# В каждом вызове функции boyer_moore_horspool, если образец найден, 
# функция выводит индекс начала вхождения. 
# Если образец не найден, функция не выводит ничего.

if func == 3:
    t = "данные"
    # Этап 1: формирование таблицы смещений
    S = set() # уникальные символы в образе
    M = len(t) # число символов в образе
    d = {} # словарь смещений
    for i in range(M-2, -1, -1): # итерации с предпоследнего символа
        if t[i] not in S: # если символ еще не добавлен в таблицу
            d[t[i]] = M-i-1
            S.add(t[i])
        if t[M-1] not in S: # отдельно формируем последний символ
            d[t[M-1]] = M
            d['*'] = M # смещения для прочих символов
            print(d)
    # Этап 2: поиск образа в строке
    a = "метеоданные"
    N = len(a)
    if N >= M:
        i = M-1 # счетчик проверяемого символа в строке
        while(i < N):
            k = 0
            j = 0
            flBreak = False
        for j in range(M-1, -1, -1):
            if a[i-k] != t[j]:
                if j == M-1:
                    off = d[a[i]] if d.get(a[i], False) else d['*'] # смещение, если не равен последний символ образа
                else:
                    off = d[t[j]] # смещение, если не равен не последний символ образа
                    i += off # смещение счетчика строки
                    flBreak = True # если несовпадение символа, то flBreak = True
                    break
                k += 1 # смещение для сравниваемого символа в строке
            if not flBreak: # если дошли до начала образа, значит, все его символы совпали
                print(f"образ найден по индексу {i-k+1}")
                break
            else:
                print("образ не найден")
        else:
            print("образ не найден")

if func == 4:
    def boyer_moore_horspool(P, T):
        pl = len(P)
        tl = len(T)
        skip_table = create_skip_table(P)
        count = 0
        i = 0

        while i <= tl - pl:
            j = pl - 1
            while j >= 0 and P[j] == T[i + j]:
                j -= 1
            if j == -1:
                count += 1
                print(i)
                i += pl
            else:
                i += max(1, j - skip_table[ord(T[i + j])])

        return count

    def create_skip_table(P):
        skip_table = {}
        for c in range(256):
            skip_table[c] = len(P)
            for i in range(len(P) - 1, -1, -1):
                if P[i] == c:
                    skip_table[c] = i + 1
                    break
        return skip_table
    
    print(boyer_moore_horspool('abc', 'ababcabcabababc'))