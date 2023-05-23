class Food:
    def __init__(self, calorises, carbs, protein, fat, nama_makanan):
        self.calories = calorises
        self.carbs = carbs 
        self.protein = protein 
        self.fat = fat
        self.nama_makanan = nama_makanan


def optimize_nutrition(food_list, calories_bound, category):

    # Fungsi untuk menghitung batas atas (upper bound) dari simpul
    def calculate_upper_bound(node, current_calories, current_value, category):
        if category == "carbs":
            upper_bound = current_value
            remaining_calories = calories_bound - current_calories
            i = node + 1
            while i < len(food_list) and food_list[i].calories <= remaining_calories:
                upper_bound += food_list[i].carbs
                remaining_calories -= food_list[i].calories
                i += 1
            if i < len(food_list):
                upper_bound += remaining_calories * (food_list[i].carbs / food_list[i].calories)

        elif category == "protein":
            upper_bound = current_value
            remaining_calories = calories_bound - current_calories
            i = node + 1
            while i < len(food_list) and food_list[i].calories <= remaining_calories:
                upper_bound += food_list[i].protein
                remaining_calories -= food_list[i].calories
                i += 1
            if i < len(food_list):
                upper_bound += remaining_calories * (food_list[i].protein / food_list[i].calories)
        
        else: 
            upper_bound = current_value
            remaining_calories = calories_bound - current_calories
            i = node + 1
            while i < len(food_list) and food_list[i].calories <= remaining_calories:
                upper_bound += food_list[i].fat
                remaining_calories -= food_list[i].calories
                i += 1
            if i < len(food_list):
                upper_bound += remaining_calories * (food_list[i].fat / food_list[i].calories)

        return upper_bound
    

    class Node:
        def __init__(self, level, calories, value, selected_items, category):
            self.level = level
            self.calories = calories
            self.value = value
            self.selected_items = selected_items
            self.upper_bound = calculate_upper_bound(level, calories, value, category)

    # Inisialisasi
    n = len(food_list)
    best_value = 0
    best_items = []

    # Stack untuk menyimpan simpul yang akan dieksplorasi
    stack = []

    # Simpul awal
    root = Node(-1, 0, 0, [], category)
    stack.append(root)

    # Proses Branch and Bound
    while stack:
        current_node = stack.pop()

        if category == "carbs":

            # Pengecekan simpul terbaik
            if current_node.value > best_value:
                best_value = current_node.value
                best_items = current_node.selected_items

            # Perluas simpul jika masih ada makanan yang tersisa
            if current_node.level < n - 1:
                next_level = current_node.level + 1
                next_calories = current_node.calories + food_list[next_level].calories
                next_value = current_node.value + food_list[next_level].carbs

                # Buat simpul baru jika batas kalori cukup
                if next_calories <= calories_bound:
                    next_items = current_node.selected_items.copy()
                    next_items.append(next_level)
                    next_node = Node(next_level, next_calories, next_value, next_items, "carbs")
                    if next_node.upper_bound > best_value:
                        stack.append(next_node)

                # Buat simpul baru tanpa memasukkan item
                without_item_node = Node(next_level, current_node.calories, current_node.value,
                                        current_node.selected_items.copy(), "carbs")
                without_item_node.upper_bound = calculate_upper_bound(without_item_node.level,
                                                                    without_item_node.calories,
                                                                    without_item_node.value,
                                                                    "carbs")
                if without_item_node.upper_bound > best_value:
                    stack.append(without_item_node)

        elif category == "protein":
            # Pengecekan simpul terbaik
            if current_node.value > best_value:
                best_value = current_node.value
                best_items = current_node.selected_items

            # Perluas simpul jika masih ada makanan yang tersisa
            if current_node.level < n - 1:
                next_level = current_node.level + 1
                next_calories = current_node.calories + food_list[next_level].calories
                next_value = current_node.value + food_list[next_level].protein

                # Buat simpul baru jika batas kalori cukup
                if next_calories <= calories_bound:
                    next_items = current_node.selected_items.copy()
                    next_items.append(next_level)
                    next_node = Node(next_level, next_calories, next_value, next_items, "protein")
                    if next_node.upper_bound > best_value:
                        stack.append(next_node)

                # Buat simpul baru tanpa memasukkan item
                without_item_node = Node(next_level, current_node.calories, current_node.value,
                                        current_node.selected_items.copy(), "protein")
                without_item_node.upper_bound = calculate_upper_bound(without_item_node.level,
                                                                    without_item_node.calories,
                                                                    without_item_node.value,
                                                                    "protein")
                if without_item_node.upper_bound > best_value:
                    stack.append(without_item_node)

        else: 
            # Pengecekan simpul terbaik
            if current_node.value > best_value:
                best_value = current_node.value
                best_items = current_node.selected_items

            # Perluas simpul jika masih ada makanan yang tersisa
            if current_node.level < n - 1:
                next_level = current_node.level + 1
                next_calories = current_node.calories + food_list[next_level].calories
                next_value = current_node.value + food_list[next_level].fat

                # Buat simpul baru jika batas kalori cukup
                if next_calories <= calories_bound:
                    next_items = current_node.selected_items.copy()
                    next_items.append(next_level)
                    next_node = Node(next_level, next_calories, next_value, next_items, "fat")
                    if next_node.upper_bound > best_value:
                        stack.append(next_node)

                # Buat simpul baru tanpa memasukkan item
                without_item_node = Node(next_level, current_node.calories, current_node.value,
                                        current_node.selected_items.copy(), "fat")
                without_item_node.upper_bound = calculate_upper_bound(without_item_node.level,
                                                                    without_item_node.calories,
                                                                    without_item_node.value,
                                                                    "fat")
                if without_item_node.upper_bound > best_value:
                    stack.append(without_item_node)


        # Urutkan simpul berdasarkan nilai batas atasnya
        stack.sort(key=lambda x: x.upper_bound, reverse=True)

    # Mengembalikan nilai terbaik dan makanan yang dipilih
    return best_value, [food_list[i] for i in best_items]
