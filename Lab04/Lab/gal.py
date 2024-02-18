{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2c4f8183",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 49 mystery mystery\n",
      "1 2\n",
      "2 3\n",
      "2 3\n",
      "4 3 1\n",
      "3 4\n",
      "5 4 2 1\n",
      "4 4\n",
      "8 3 5 2\n",
      "5 7\n",
      "15 11 8 9 6 3 4\n",
      "6 2\n",
      "9 5\n",
      "7 3\n",
      "14 13 8\n",
      "8 5\n",
      "12 11 5 4 7\n",
      "9 6\n",
      "26 22 15 10 6 5\n",
      "10 3\n",
      "20 17 9\n",
      "11 4\n",
      "16 12 5 8\n",
      "12 5\n",
      "16 14 13 11 8\n",
      "13 3\n",
      "14 12 7\n",
      "14 6\n",
      "19 12 13 16 18 7\n",
      "15 4\n",
      "25 16 5 9\n",
      "16 7\n",
      "25 24 18 15 11 12 14\n",
      "17 3\n",
      "23 20 10\n",
      "18 4\n",
      "24 19 16 14\n",
      "19 3\n",
      "18 24 14\n",
      "20 9\n",
      "35 33 27 22 23 32 40 17 10\n",
      "21 4\n",
      "34 24 30 9\n",
      "22 5\n",
      "28 27 26 20 9\n",
      "23 3\n",
      "32 17 20\n",
      "24 6\n",
      "30 25 16 18 21 19\n",
      "25 5\n",
      "29 15 26 16 24\n",
      "26 4\n",
      "28 22 9 25\n",
      "27 4\n",
      "33 28 20 22\n",
      "28 7\n",
      "38 29 27 33 35 22 26\n",
      "29 4\n",
      "37 30 28 25\n",
      "30 4\n",
      "37 29 24 21\n",
      "31 2\n",
      "36 34\n",
      "32 4\n",
      "41 40 23 20\n",
      "33 4\n",
      "35 20 27 28\n",
      "34 4\n",
      "42 36 21 31\n",
      "35 5\n",
      "44 38 20 33 28\n",
      "36 5\n",
      "46 39 34 42 31\n",
      "37 5\n",
      "45 38 43 29 30\n",
      "38 4\n",
      "43 35 28 37\n",
      "39 2\n",
      "46 36\n",
      "40 4\n",
      "47 41 32 20\n",
      "41 3\n",
      "47 32 40\n",
      "42 2\n",
      "34 36\n",
      "43 5\n",
      "48 45 44 38 37\n",
      "44 4\n",
      "49 48 35 43\n",
      "45 4\n",
      "48 49 37 43\n",
      "46 2\n",
      "36 39\n",
      "47 2\n",
      "40 41\n",
      "48 4\n",
      "49 44 43 45\n",
      "49 3\n",
      "44 48 45\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Read in Lab04-1.gal\n",
    "with open(r\"C:\\Users\\manue\\OneDrive - University of Glasgow\\URBAN5123 - Programming Tools for UA\\Labs\\PTUA2024\\Lab04\\Lab\\Lab04-1.gal\", \"r\") as f:\n",
    "    file_content = f.read()\n",
    "print(file_content)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "73940d18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['0 49 mystery mystery', '1 2', '2 3', '2 3', '4 3 1', '3 4', '5 4 2 1', '4 4', '8 3 5 2', '5 7', '15 11 8 9 6 3 4', '6 2', '9 5', '7 3', '14 13 8', '8 5', '12 11 5 4 7', '9 6', '26 22 15 10 6 5', '10 3', '20 17 9', '11 4', '16 12 5 8', '12 5', '16 14 13 11 8', '13 3', '14 12 7', '14 6', '19 12 13 16 18 7', '15 4', '25 16 5 9', '16 7', '25 24 18 15 11 12 14', '17 3', '23 20 10', '18 4', '24 19 16 14', '19 3', '18 24 14', '20 9', '35 33 27 22 23 32 40 17 10', '21 4', '34 24 30 9', '22 5', '28 27 26 20 9', '23 3', '32 17 20', '24 6', '30 25 16 18 21 19', '25 5', '29 15 26 16 24', '26 4', '28 22 9 25', '27 4', '33 28 20 22', '28 7', '38 29 27 33 35 22 26', '29 4', '37 30 28 25', '30 4', '37 29 24 21', '31 2', '36 34', '32 4', '41 40 23 20', '33 4', '35 20 27 28', '34 4', '42 36 21 31', '35 5', '44 38 20 33 28', '36 5', '46 39 34 42 31', '37 5', '45 38 43 29 30', '38 4', '43 35 28 37', '39 2', '46 36', '40 4', '47 41 32 20', '41 3', '47 32 40', '42 2', '34 36', '43 5', '48 45 44 38 37', '44 4', '49 48 35 43', '45 4', '48 49 37 43', '46 2', '36 39', '47 2', '40 41', '48 4', '49 44 43 45', '49 3', '44 48 45']\n"
     ]
    }
   ],
   "source": [
    "# Save the contents to a list (assuming each line is a separate item)\n",
    "data = file_content.splitlines()\n",
    "\n",
    "# Print the object to confirm\n",
    "print(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e76ce1c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['1 2', '2 3', '2 3', '4 3 1', '3 4', '5 4 2 1', '4 4', '8 3 5 2', '5 7', '15 11 8 9 6 3 4', '6 2', '9 5', '7 3', '14 13 8', '8 5', '12 11 5 4 7', '9 6', '26 22 15 10 6 5', '10 3', '20 17 9', '11 4', '16 12 5 8', '12 5', '16 14 13 11 8', '13 3', '14 12 7', '14 6', '19 12 13 16 18 7', '15 4', '25 16 5 9', '16 7', '25 24 18 15 11 12 14', '17 3', '23 20 10', '18 4', '24 19 16 14', '19 3', '18 24 14', '20 9', '35 33 27 22 23 32 40 17 10', '21 4', '34 24 30 9', '22 5', '28 27 26 20 9', '23 3', '32 17 20', '24 6', '30 25 16 18 21 19', '25 5', '29 15 26 16 24', '26 4', '28 22 9 25', '27 4', '33 28 20 22', '28 7', '38 29 27 33 35 22 26', '29 4', '37 30 28 25', '30 4', '37 29 24 21', '31 2', '36 34', '32 4', '41 40 23 20', '33 4', '35 20 27 28', '34 4', '42 36 21 31', '35 5', '44 38 20 33 28', '36 5', '46 39 34 42 31', '37 5', '45 38 43 29 30', '38 4', '43 35 28 37', '39 2', '46 36', '40 4', '47 41 32 20', '41 3', '47 32 40', '42 2', '34 36', '43 5', '48 45 44 38 37', '44 4', '49 48 35 43', '45 4', '48 49 37 43', '46 2', '36 39', '47 2', '40 41', '48 4', '49 44 43 45', '49 3', '44 48 45']\n"
     ]
    }
   ],
   "source": [
    "# Delete first element in data\n",
    "del(data[0])\n",
    "print(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d3d27106",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(1, 2), (2, 3), (2, 3), (4, 3, 1), (3, 4), (5, 4, 2, 1), (4, 4), (8, 3, 5, 2), (5, 7), (15, 11, 8, 9, 6, 3, 4), (6, 2), (9, 5), (7, 3), (14, 13, 8), (8, 5), (12, 11, 5, 4, 7), (9, 6), (26, 22, 15, 10, 6, 5), (10, 3), (20, 17, 9), (11, 4), (16, 12, 5, 8), (12, 5), (16, 14, 13, 11, 8), (13, 3), (14, 12, 7), (14, 6), (19, 12, 13, 16, 18, 7), (15, 4), (25, 16, 5, 9), (16, 7), (25, 24, 18, 15, 11, 12, 14), (17, 3), (23, 20, 10), (18, 4), (24, 19, 16, 14), (19, 3), (18, 24, 14), (20, 9), (35, 33, 27, 22, 23, 32, 40, 17, 10), (21, 4), (34, 24, 30, 9), (22, 5), (28, 27, 26, 20, 9), (23, 3), (32, 17, 20), (24, 6), (30, 25, 16, 18, 21, 19), (25, 5), (29, 15, 26, 16, 24), (26, 4), (28, 22, 9, 25), (27, 4), (33, 28, 20, 22), (28, 7), (38, 29, 27, 33, 35, 22, 26), (29, 4), (37, 30, 28, 25), (30, 4), (37, 29, 24, 21), (31, 2), (36, 34), (32, 4), (41, 40, 23, 20), (33, 4), (35, 20, 27, 28), (34, 4), (42, 36, 21, 31), (35, 5), (44, 38, 20, 33, 28), (36, 5), (46, 39, 34, 42, 31), (37, 5), (45, 38, 43, 29, 30), (38, 4), (43, 35, 28, 37), (39, 2), (46, 36), (40, 4), (47, 41, 32, 20), (41, 3), (47, 32, 40), (42, 2), (34, 36), (43, 5), (48, 45, 44, 38, 37), (44, 4), (49, 48, 35, 43), (45, 4), (48, 49, 37, 43), (46, 2), (36, 39), (47, 2), (40, 41), (48, 4), (49, 44, 43, 45), (49, 3), (44, 48, 45)]\n"
     ]
    }
   ],
   "source": [
    "# Split each string into a list of integers\n",
    "list_of_lists = [[int(x) for x in item.split()] for item in data]\n",
    "\n",
    "# Convert the list of lists to a list of tuples\n",
    "tuple_list = [(item[0], *item[1:]) for item in list_of_lists]\n",
    "print(tuple_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "24162e29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: [2, 3], 2: [4, 3, 1], 3: [5, 4, 2, 1], 4: [8, 3, 5, 2], 5: [15, 11, 8, 9, 6, 3, 4], 6: [9, 5], 7: [14, 13, 8], 8: [12, 11, 5, 4, 7], 9: [26, 22, 15, 10, 6, 5], 10: [20, 17, 9], 11: [16, 12, 5, 8], 12: [16, 14, 13, 11, 8], 13: [14, 12, 7], 14: [19, 12, 13, 16, 18, 7], 15: [25, 16, 5, 9], 16: [25, 24, 18, 15, 11, 12, 14], 17: [23, 20, 10], 18: [24, 19, 16, 14], 19: [18, 24, 14], 20: [35, 33, 27, 22, 23, 32, 40, 17, 10], 21: [34, 24, 30, 9], 22: [28, 27, 26, 20, 9], 23: [32, 17, 20], 24: [30, 25, 16, 18, 21, 19], 25: [29, 15, 26, 16, 24], 26: [28, 22, 9, 25], 27: [33, 28, 20, 22], 28: [38, 29, 27, 33, 35, 22, 26], 29: [37, 30, 28, 25], 30: [37, 29, 24, 21], 31: [36, 34], 32: [41, 40, 23, 20], 33: [35, 20, 27, 28], 34: [42, 36, 21, 31], 35: [44, 38, 20, 33, 28], 36: [46, 39, 34, 42, 31], 37: [45, 38, 43, 29, 30], 38: [43, 35, 28, 37], 39: [46, 36], 40: [47, 41, 32, 20], 41: [47, 32, 40], 42: [34, 36], 43: [48, 45, 44, 38, 37], 44: [49, 48, 35, 43], 45: [48, 49, 37, 43], 46: [36, 39], 47: [40, 41], 48: [49, 44, 43, 45], 49: [44, 48, 45]}\n"
     ]
    }
   ],
   "source": [
    "# Return a Python dictionary where the key is the id of a spatial unit and the value is a list of the ids of its neighbors.\n",
    "gal_dict = {}\n",
    "key = None\n",
    "values = []\n",
    "\n",
    "for i, element in enumerate(tuple_list):\n",
    "    if i % 2 == 0:\n",
    "        if key is not None:\n",
    "            gal_dict[key] = values\n",
    "        key = element[0]\n",
    "        values = []\n",
    "    else:\n",
    "        values.extend(element)  # Add all elements from odd-indexed tuples to values\n",
    "\n",
    "# Add the last key-value pair\n",
    "gal_dict[key] = values\n",
    "\n",
    "print(gal_dict)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "a952c9f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{2: [1, 6, 31, 39, 42, 46, 47], 3: [2, 7, 10, 13, 17, 19, 23, 41, 49], 4: [3, 4, 11, 15, 18, 21, 26, 27, 29, 30, 32, 33, 34, 38, 40, 44, 45, 48], 7: [5, 16, 28], 5: [8, 12, 22, 25, 35, 36, 37, 43], 6: [9, 14, 24], 9: [20]}\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAiMAAAGdCAYAAADAAnMpAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAAAdgklEQVR4nO3df3RX9X348VcIklAGcUIJRAKG1h8cc7Q7wa4BmbNqeoBxttOewo5rsfw4a04oCJmuIDtTmTNtT8thnQXKFNHW0pz+sGvXVMx2joilOwMaZls41RbbUAzNCe1I1J5QyN0ffsl3aYL1E+XzNuTxOOf+8Xnn3nxe93Pi4en9/CrIsiwLAIBERqQeAAAY3sQIAJCUGAEAkhIjAEBSYgQASEqMAABJiREAICkxAgAkNTL1AK9HT09PvPjiizF27NgoKChIPQ4A8DpkWRZdXV1RVlYWI0ac+/rHkIiRF198McrLy1OPAQAMwtGjR2PKlCnn/PmQiJGxY8dGxKsnM27cuMTTAACvR2dnZ5SXl/f+O34uQyJGzj41M27cODECAEPM73uJhRewAgBJiREAICkxAgAkJUYAgKTECACQlBgBAJISIwBAUmIEAEhKjAAASYkRACCpnGPk6aefjgULFkRZWVkUFBTEN77xjd97zO7du6OqqiqKi4tj+vTpsXXr1sHMCgBcgHKOkZdffjmuvfbaeOCBB17X/i+88ELMmzcv5syZEy0tLXHXXXfFqlWr4mtf+1rOwwIAF56cvyhv7ty5MXfu3Ne9/9atW2Pq1KmxadOmiIiYMWNG7N+/Pz796U/HBz7wgVzvHgC4wJz314x873vfi5qamj5r73vf+2L//v3x29/+dsBjuru7o7Ozs88GAFyYcr4ykqvjx49HaWlpn7XS0tI4ffp0dHR0xOTJk/sd09DQEPfee+/5Hi0iIi5b++283A9D088+MT/1CDnzN50f/jbyw+OcH6kf57y8m6agoKDP7SzLBlw/a926dXHy5Mne7ejRo+d9RgAgjfN+ZWTSpElx/PjxPmvt7e0xcuTIGD9+/IDHFBUVRVFR0fkeDQB4CzjvV0aqq6ujubm5z9qTTz4ZM2fOjIsuuuh83z0A8BaXc4y89NJLcfDgwTh48GBEvPrW3YMHD0Zra2tEvPoUy+LFi3v3r62tjZ///OdRX18fhw8fju3bt8dDDz0Ud9xxx5tzBgDAkJbz0zT79++PG2+8sfd2fX19RETcdtttsWPHjmhra+sNk4iIioqKaGpqijVr1sTnPve5KCsri89+9rPe1gsARMQgYuRP//RPe1+AOpAdO3b0W7vhhhvi+9//fq53BQAMA76bBgBISowAAEmJEQAgKTECACQlRgCApMQIAJCUGAEAkhIjAEBSYgQASEqMAABJiREAICkxAgAkJUYAgKTECACQlBgBAJISIwBAUmIEAEhKjAAASYkRACApMQIAJCVGAICkxAgAkJQYAQCSEiMAQFJiBABISowAAEmJEQAgKTECACQlRgCApMQIAJCUGAEAkhIjAEBSYgQASEqMAABJiREAICkxAgAkJUYAgKTECACQlBgBAJISIwBAUmIEAEhKjAAASYkRACApMQIAJCVGAICkxAgAkJQYAQCSEiMAQFJiBABISowAAEmJEQAgKTECACQlRgCApMQIAJCUGAEAkhIjAEBSYgQASEqMAABJiREAICkxAgAkNagY2bx5c1RUVERxcXFUVVXFnj17XnP/xx57LK699tp429veFpMnT44lS5bEiRMnBjUwAHBhyTlGGhsbY/Xq1bF+/fpoaWmJOXPmxNy5c6O1tXXA/Z955plYvHhxLFu2LH70ox/FV77yldi3b18sX778DQ8PAAx9OcfIxo0bY9myZbF8+fKYMWNGbNq0KcrLy2PLli0D7v+f//mfcdlll8WqVauioqIirr/++vjoRz8a+/fvf8PDAwBDX04xcurUqThw4EDU1NT0Wa+pqYm9e/cOeMysWbPiF7/4RTQ1NUWWZfHLX/4yvvrVr8b8+fPPeT/d3d3R2dnZZwMALkw5xUhHR0ecOXMmSktL+6yXlpbG8ePHBzxm1qxZ8dhjj8WiRYti1KhRMWnSpLj44ovjn//5n895Pw0NDVFSUtK7lZeX5zImADCEDOoFrAUFBX1uZ1nWb+2sQ4cOxapVq+Lv//7v48CBA/HEE0/ECy+8ELW1tef8/evWrYuTJ0/2bkePHh3MmADAEDAyl50nTJgQhYWF/a6CtLe397taclZDQ0PMnj077rzzzoiIuOaaa2LMmDExZ86cuO+++2Ly5Mn9jikqKoqioqJcRgMAhqicroyMGjUqqqqqorm5uc96c3NzzJo1a8BjXnnllRgxou/dFBYWRsSrV1QAgOEt56dp6uvr48EHH4zt27fH4cOHY82aNdHa2tr7tMu6deti8eLFvfsvWLAgvv71r8eWLVviyJEj8d3vfjdWrVoV7373u6OsrOzNOxMAYEjK6WmaiIhFixbFiRMnYsOGDdHW1haVlZXR1NQU06ZNi4iItra2Pp858pGPfCS6urrigQceiL/5m7+Jiy++ON773vfGJz/5yTfvLACAISvnGImIqKuri7q6ugF/tmPHjn5rK1eujJUrVw7mrgCAC5zvpgEAkhIjAEBSYgQASEqMAABJiREAICkxAgAkJUYAgKTECACQlBgBAJISIwBAUmIEAEhKjAAASYkRACApMQIAJCVGAICkxAgAkJQYAQCSEiMAQFJiBABISowAAEmJEQAgKTECACQlRgCApMQIAJCUGAEAkhIjAEBSYgQASEqMAABJiREAICkxAgAkJUYAgKTECACQlBgBAJISIwBAUmIEAEhKjAAASYkRACApMQIAJCVGAICkxAgAkJQYAQCSEiMAQFJiBABISowAAEmJEQAgKTECACQlRgCApMQIAJCUGAEAkhIjAEBSYgQASEqMAABJiREAICkxAgAkJUYAgKTECACQlBgBAJISIwBAUmIEAEhqUDGyefPmqKioiOLi4qiqqoo9e/a85v7d3d2xfv36mDZtWhQVFcU73vGO2L59+6AGBgAuLCNzPaCxsTFWr14dmzdvjtmzZ8fnP//5mDt3bhw6dCimTp064DELFy6MX/7yl/HQQw/FO9/5zmhvb4/Tp0+/4eEBgKEv5xjZuHFjLFu2LJYvXx4REZs2bYpdu3bFli1boqGhod/+TzzxROzevTuOHDkSl1xySUREXHbZZW9sagDggpHT0zSnTp2KAwcORE1NTZ/1mpqa2Lt374DHfPOb34yZM2fGpz71qbj00kvjiiuuiDvuuCN+85vfnPN+uru7o7Ozs88GAFyYcroy0tHREWfOnInS0tI+66WlpXH8+PEBjzly5Eg888wzUVxcHI8//nh0dHREXV1d/OpXvzrn60YaGhri3nvvzWU0AGCIGtQLWAsKCvrczrKs39pZPT09UVBQEI899li8+93vjnnz5sXGjRtjx44d57w6sm7dujh58mTvdvTo0cGMCQAMATldGZkwYUIUFhb2uwrS3t7e72rJWZMnT45LL700SkpKetdmzJgRWZbFL37xi7j88sv7HVNUVBRFRUW5jAYADFE5XRkZNWpUVFVVRXNzc5/15ubmmDVr1oDHzJ49O1588cV46aWXeteee+65GDFiREyZMmUQIwMAF5Kcn6apr6+PBx98MLZv3x6HDx+ONWvWRGtra9TW1kbEq0+xLF68uHf/W2+9NcaPHx9LliyJQ4cOxdNPPx133nlnLF26NEaPHv3mnQkAMCTl/NbeRYsWxYkTJ2LDhg3R1tYWlZWV0dTUFNOmTYuIiLa2tmhtbe3d/w/+4A+iubk5Vq5cGTNnzozx48fHwoUL47777nvzzgIAGLJyjpGIiLq6uqirqxvwZzt27Oi3dtVVV/V7agcAIMJ30wAAiYkRACApMQIAJCVGAICkxAgAkJQYAQCSEiMAQFJiBABISowAAEmJEQAgKTECACQlRgCApMQIAJCUGAEAkhIjAEBSYgQASEqMAABJiREAICkxAgAkJUYAgKTECACQlBgBAJISIwBAUmIEAEhKjAAASYkRACApMQIAJCVGAICkxAgAkJQYAQCSEiMAQFJiBABISowAAEmJEQAgKTECACQlRgCApMQIAJCUGAEAkhIjAEBSYgQASEqMAABJiREAICkxAgAkJUYAgKTECACQlBgBAJISIwBAUmIEAEhKjAAASYkRACApMQIAJCVGAICkxAgAkJQYAQCSEiMAQFJiBABISowAAEmJEQAgKTECACQ1qBjZvHlzVFRURHFxcVRVVcWePXte13Hf/e53Y+TIkfGud71rMHcLAFyAco6RxsbGWL16daxfvz5aWlpizpw5MXfu3GhtbX3N406ePBmLFy+Om266adDDAgAXnpxjZOPGjbFs2bJYvnx5zJgxIzZt2hTl5eWxZcuW1zzuox/9aNx6661RXV096GEBgAtPTjFy6tSpOHDgQNTU1PRZr6mpib17957zuIcffjh++tOfxt133/267qe7uzs6Ozv7bADAhSmnGOno6IgzZ85EaWlpn/XS0tI4fvz4gMc8//zzsXbt2njsscdi5MiRr+t+GhoaoqSkpHcrLy/PZUwAYAgZ1AtYCwoK+tzOsqzfWkTEmTNn4tZbb4177703rrjiitf9+9etWxcnT57s3Y4ePTqYMQGAIeD1Xar4fyZMmBCFhYX9roK0t7f3u1oSEdHV1RX79++PlpaW+NjHPhYRET09PZFlWYwcOTKefPLJeO9739vvuKKioigqKsplNABgiMrp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o7y8PI4ePRrjxo17037vUDLcH4Phfv4RHgPnP7zPP8JjcD7PP8uy6OrqirKystfcL6cYmTBhQhQWFva7CtLe3t7v6sdZkyZNGnD/kSNHxvjx4wc8pqioKIqKivqsXXzxxbmMmpNx48YNyz/A/2u4PwbD/fwjPAbOf3iff4TH4Hyd/2tdETkrpxewjho1KqqqqqK5ubnPenNzc8yaNWvAY6qrq/vt/+STT8bMmTMHfL0IADC85Pxumvr6+njwwQdj+/btcfjw4VizZk20trZGbW1tRLz6FMvixYt796+trY2f//znUV9fH4cPH47t27fHQw89FHfcccebdxYAwJCV82tGFi1aFCdOnIgNGzZEW1tbVFZWRlNTU0ybNi0iItra2vp85khFRUU0NTXFmjVr4nOf+1yUlZXFZz/72fjABz7w5p3FIBUVFcXdd9/d7ymh4WS4PwbD/fwjPAbOf3iff4TH4K1w/gXZ73u/DQDAeeS7aQCApMQIAJCUGAEAkhIjAEBSwzJGGhoa4rrrrouxY8fGxIkT4y/+4i/ixz/+ceqx8mbLli1xzTXX9H7ATXV1dXznO99JPVYyDQ0NUVBQEKtXr049St7cc889UVBQ0GebNGlS6rHy7tixY/GhD30oxo8fH29729viXe96Vxw4cCD1WHlx2WWX9fsbKCgoiBUrVqQeLS9Onz4df/d3fxcVFRUxevTomD59emzYsCF6enpSj5ZXXV1dsXr16pg2bVqMHj06Zs2aFfv27cv7HIP6OPihbvfu3bFixYq47rrr4vTp07F+/fqoqamJQ4cOxZgxY1KPd95NmTIlPvGJT8Q73/nOiIh45JFH4s///M+jpaUlrr766sTT5de+ffti27Ztcc0116QeJe+uvvrq+Pd///fe24WFhQmnyb9f//rXMXv27LjxxhvjO9/5TkycODF++tOfntdPe34r2bdvX5w5c6b39g9/+MO45ZZb4oMf/GDCqfLnk5/8ZGzdujUeeeSRuPrqq2P//v2xZMmSKCkpidtvvz31eHmzfPny+OEPfxhf+MIXoqysLL74xS/GzTffHIcOHYpLL700f4NkZO3t7VlEZLt37049SjJ/+Id/mD344IOpx8irrq6u7PLLL8+am5uzG264Ibv99ttTj5Q3d999d3bttdemHiOpj3/849n111+feoy3jNtvvz17xzvekfX09KQeJS/mz5+fLV26tM/a+9///uxDH/pQoony75VXXskKCwuzf/u3f+uzfu2112br16/P6yzD8mma33Xy5MmIiLjkkksST5J/Z86ciS9/+cvx8ssvR3V1depx8mrFihUxf/78uPnmm1OPksTzzz8fZWVlUVFREX/5l38ZR44cST1SXn3zm9+MmTNnxgc/+MGYOHFi/NEf/VH8y7/8S+qxkjh16lR88YtfjKVLl76pX0b6Vnb99dfHf/zHf8Rzzz0XERH//d//Hc8880zMmzcv8WT5c/r06Thz5kwUFxf3WR89enQ888wz+R0mr+nzFtTT05MtWLBg2P0f0rPPPpuNGTMmKywszEpKSrJvf/vbqUfKq507d2aVlZXZb37zmyzLsmF3ZaSpqSn76le/mj377LO9V4ZKS0uzjo6O1KPlTVFRUVZUVJStW7cu+/73v59t3bo1Ky4uzh555JHUo+VdY2NjVlhYmB07diz1KHnT09OTrV27NisoKMhGjhyZFRQUZPfff3/qsfKuuro6u+GGG7Jjx45lp0+fzr7whS9kBQUF2RVXXJHXOYZ9jNTV1WXTpk3Ljh49mnqUvOru7s6ef/75bN++fdnatWuzCRMmZD/60Y9Sj5UXra2t2cSJE7ODBw/2rg23GPldL730UlZaWpp95jOfST1K3lx00UVZdXV1n7WVK1dm73nPexJNlE5NTU32Z3/2Z6nHyKudO3dmU6ZMyXbu3Jk9++yz2aOPPppdcskl2Y4dO1KPllc/+clPsj/5kz/JIiIrLCzMrrvuuuyv/uqvshkzZuR1jmEdIx/72MeyKVOmZEeOHEk9SnI33XRT9td//depx8iLxx9/vPc/vLNbRGQFBQVZYWFhdvr06dQjJnHzzTdntbW1qcfIm6lTp2bLli3rs7Z58+asrKws0URp/OxnP8tGjBiRfeMb30g9Sl5NmTIle+CBB/qs/cM//EN25ZVXJpoorZdeeil78cUXsyzLsoULF2bz5s3L6/0Py3fTZFkWK1eujMcffzyeeuqpqKioSD1SclmWRXd3d+ox8uKmm26KH/zgB33WlixZEldddVV8/OMfH3bvKomI6O7ujsOHD8ecOXNSj5I3s2fP7veW/ueee673Sz+Hi4cffjgmTpwY8+fPTz1KXr3yyisxYkTfl00WFhYOu7f2njVmzJgYM2ZM/PrXv45du3bFpz71qbze/7CMkRUrVsSXvvSl+Nd//dcYO3ZsHD9+PCIiSkpKYvTo0YmnO//uuuuumDt3bpSXl0dXV1d8+ctfjqeeeiqeeOKJ1KPlxdixY6OysrLP2pgxY2L8+PH91i9Ud9xxRyxYsCCmTp0a7e3tcd9990VnZ2fcdtttqUfLmzVr1sSsWbPi/vvvj4ULF8Z//dd/xbZt22Lbtm2pR8ubnp6eePjhh+O2226LkSOH1z8HCxYsiH/8x3+MqVOnxtVXXx0tLS2xcePGWLp0aerR8mrXrl2RZVlceeWV8ZOf/CTuvPPOuPLKK2PJkiX5HSSv12HeIiJiwO3hhx9OPVpeLF26NJs2bVo2atSo7O1vf3t20003ZU8++WTqsZIabq8ZWbRoUTZ58uTsoosuysrKyrL3v//9w+Y1Q//Xt771rayysjIrKirKrrrqqmzbtm2pR8qrXbt2ZRGR/fjHP049St51dnZmt99+ezZ16tSsuLg4mz59erZ+/fqsu7s79Wh51djYmE2fPj0bNWpUNmnSpGzFihXZ//zP/+R9joIsy7L85g8AwP/nc0YAgKTECACQlBgBAJISIwBAUmIEAEhKjAAASYkRACApMQIAJCVGAICkxAgAkJQYAQCSEiMAQFL/CzZSslmT4SLDAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Take a gal dictionary from 1 and return a second dictionary that has the histogram for the neighbor cardinalities.\n",
    "# In the second dictionary, the key is the number of neighbors and the value is the list of ids that have key neighbors.\n",
    "# It is up to you if you want to draw the histogram.\n",
    "\n",
    "dict_2 = {}\n",
    "for key, val in gal_dict.items():\n",
    "    value_count = len(val)\n",
    "    if value_count in dict_2:\n",
    "        dict_2[value_count].append(key)\n",
    "    else:\n",
    "        dict_2[value_count] = [key]\n",
    "\n",
    "print(dict_2)\n",
    "\n",
    "# Histogram\n",
    "import matplotlib.pyplot as plt\n",
    "plt.hist(dict_2)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "0d499a85",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 [2, 3]\n",
      "1  says  2 is a neighbor\n",
      "ok\n",
      "1  says  3 is a neighbor\n",
      "ok\n",
      "2 [4, 3, 1]\n",
      "2  says  4 is a neighbor\n",
      "ok\n",
      "2  says  3 is a neighbor\n",
      "ok\n",
      "2  says  1 is a neighbor\n",
      "ok\n",
      "3 [5, 4, 2, 1]\n",
      "3  says  5 is a neighbor\n",
      "ok\n",
      "3  says  4 is a neighbor\n",
      "ok\n",
      "3  says  2 is a neighbor\n",
      "ok\n",
      "3  says  1 is a neighbor\n",
      "ok\n",
      "4 [8, 3, 5, 2]\n",
      "4  says  8 is a neighbor\n",
      "ok\n",
      "4  says  3 is a neighbor\n",
      "ok\n",
      "4  says  5 is a neighbor\n",
      "ok\n",
      "4  says  2 is a neighbor\n",
      "ok\n",
      "5 [15, 11, 8, 9, 6, 3, 4]\n",
      "5  says  15 is a neighbor\n",
      "ok\n",
      "5  says  11 is a neighbor\n",
      "ok\n",
      "5  says  8 is a neighbor\n",
      "ok\n",
      "5  says  9 is a neighbor\n",
      "ok\n",
      "5  says  6 is a neighbor\n",
      "ok\n",
      "5  says  3 is a neighbor\n",
      "ok\n",
      "5  says  4 is a neighbor\n",
      "ok\n",
      "6 [9, 5]\n",
      "6  says  9 is a neighbor\n",
      "ok\n",
      "6  says  5 is a neighbor\n",
      "ok\n",
      "7 [14, 13, 8]\n",
      "7  says  14 is a neighbor\n",
      "ok\n",
      "7  says  13 is a neighbor\n",
      "ok\n",
      "7  says  8 is a neighbor\n",
      "ok\n",
      "8 [12, 11, 5, 4, 7]\n",
      "8  says  12 is a neighbor\n",
      "ok\n",
      "8  says  11 is a neighbor\n",
      "ok\n",
      "8  says  5 is a neighbor\n",
      "ok\n",
      "8  says  4 is a neighbor\n",
      "ok\n",
      "8  says  7 is a neighbor\n",
      "ok\n",
      "9 [26, 22, 15, 10, 6, 5]\n",
      "9  says  26 is a neighbor\n",
      "ok\n",
      "9  says  22 is a neighbor\n",
      "ok\n",
      "9  says  15 is a neighbor\n",
      "ok\n",
      "9  says  10 is a neighbor\n",
      "ok\n",
      "9  says  6 is a neighbor\n",
      "ok\n",
      "9  says  5 is a neighbor\n",
      "ok\n",
      "10 [20, 17, 9]\n",
      "10  says  20 is a neighbor\n",
      "ok\n",
      "10  says  17 is a neighbor\n",
      "ok\n",
      "10  says  9 is a neighbor\n",
      "ok\n",
      "11 [16, 12, 5, 8]\n",
      "11  says  16 is a neighbor\n",
      "ok\n",
      "11  says  12 is a neighbor\n",
      "ok\n",
      "11  says  5 is a neighbor\n",
      "ok\n",
      "11  says  8 is a neighbor\n",
      "ok\n",
      "12 [16, 14, 13, 11, 8]\n",
      "12  says  16 is a neighbor\n",
      "ok\n",
      "12  says  14 is a neighbor\n",
      "ok\n",
      "12  says  13 is a neighbor\n",
      "ok\n",
      "12  says  11 is a neighbor\n",
      "ok\n",
      "12  says  8 is a neighbor\n",
      "ok\n",
      "13 [14, 12, 7]\n",
      "13  says  14 is a neighbor\n",
      "ok\n",
      "13  says  12 is a neighbor\n",
      "ok\n",
      "13  says  7 is a neighbor\n",
      "ok\n",
      "14 [19, 12, 13, 16, 18, 7]\n",
      "14  says  19 is a neighbor\n",
      "ok\n",
      "14  says  12 is a neighbor\n",
      "ok\n",
      "14  says  13 is a neighbor\n",
      "ok\n",
      "14  says  16 is a neighbor\n",
      "ok\n",
      "14  says  18 is a neighbor\n",
      "ok\n",
      "14  says  7 is a neighbor\n",
      "ok\n",
      "15 [25, 16, 5, 9]\n",
      "15  says  25 is a neighbor\n",
      "ok\n",
      "15  says  16 is a neighbor\n",
      "ok\n",
      "15  says  5 is a neighbor\n",
      "ok\n",
      "15  says  9 is a neighbor\n",
      "ok\n",
      "16 [25, 24, 18, 15, 11, 12, 14]\n",
      "16  says  25 is a neighbor\n",
      "ok\n",
      "16  says  24 is a neighbor\n",
      "ok\n",
      "16  says  18 is a neighbor\n",
      "ok\n",
      "16  says  15 is a neighbor\n",
      "ok\n",
      "16  says  11 is a neighbor\n",
      "ok\n",
      "16  says  12 is a neighbor\n",
      "ok\n",
      "16  says  14 is a neighbor\n",
      "ok\n",
      "17 [23, 20, 10]\n",
      "17  says  23 is a neighbor\n",
      "ok\n",
      "17  says  20 is a neighbor\n",
      "ok\n",
      "17  says  10 is a neighbor\n",
      "ok\n",
      "18 [24, 19, 16, 14]\n",
      "18  says  24 is a neighbor\n",
      "ok\n",
      "18  says  19 is a neighbor\n",
      "ok\n",
      "18  says  16 is a neighbor\n",
      "ok\n",
      "18  says  14 is a neighbor\n",
      "ok\n",
      "19 [18, 24, 14]\n",
      "19  says  18 is a neighbor\n",
      "ok\n",
      "19  says  24 is a neighbor\n",
      "ok\n",
      "19  says  14 is a neighbor\n",
      "ok\n",
      "20 [35, 33, 27, 22, 23, 32, 40, 17, 10]\n",
      "20  says  35 is a neighbor\n",
      "ok\n",
      "20  says  33 is a neighbor\n",
      "ok\n",
      "20  says  27 is a neighbor\n",
      "ok\n",
      "20  says  22 is a neighbor\n",
      "ok\n",
      "20  says  23 is a neighbor\n",
      "ok\n",
      "20  says  32 is a neighbor\n",
      "ok\n",
      "20  says  40 is a neighbor\n",
      "ok\n",
      "20  says  17 is a neighbor\n",
      "ok\n",
      "20  says  10 is a neighbor\n",
      "ok\n",
      "21 [34, 24, 30, 9]\n",
      "21  says  34 is a neighbor\n",
      "ok\n",
      "21  says  24 is a neighbor\n",
      "ok\n",
      "21  says  30 is a neighbor\n",
      "ok\n",
      "21  says  9 is a neighbor\n",
      "not ok\n",
      "because  9  says that  21 is not a neighbor\n",
      "22 [28, 27, 26, 20, 9]\n",
      "22  says  28 is a neighbor\n",
      "ok\n",
      "22  says  27 is a neighbor\n",
      "ok\n",
      "22  says  26 is a neighbor\n",
      "ok\n",
      "22  says  20 is a neighbor\n",
      "ok\n",
      "22  says  9 is a neighbor\n",
      "ok\n",
      "23 [32, 17, 20]\n",
      "23  says  32 is a neighbor\n",
      "ok\n",
      "23  says  17 is a neighbor\n",
      "ok\n",
      "23  says  20 is a neighbor\n",
      "ok\n",
      "24 [30, 25, 16, 18, 21, 19]\n",
      "24  says  30 is a neighbor\n",
      "ok\n",
      "24  says  25 is a neighbor\n",
      "ok\n",
      "24  says  16 is a neighbor\n",
      "ok\n",
      "24  says  18 is a neighbor\n",
      "ok\n",
      "24  says  21 is a neighbor\n",
      "ok\n",
      "24  says  19 is a neighbor\n",
      "ok\n",
      "25 [29, 15, 26, 16, 24]\n",
      "25  says  29 is a neighbor\n",
      "ok\n",
      "25  says  15 is a neighbor\n",
      "ok\n",
      "25  says  26 is a neighbor\n",
      "ok\n",
      "25  says  16 is a neighbor\n",
      "ok\n",
      "25  says  24 is a neighbor\n",
      "ok\n",
      "26 [28, 22, 9, 25]\n",
      "26  says  28 is a neighbor\n",
      "ok\n",
      "26  says  22 is a neighbor\n",
      "ok\n",
      "26  says  9 is a neighbor\n",
      "ok\n",
      "26  says  25 is a neighbor\n",
      "ok\n",
      "27 [33, 28, 20, 22]\n",
      "27  says  33 is a neighbor\n",
      "ok\n",
      "27  says  28 is a neighbor\n",
      "ok\n",
      "27  says  20 is a neighbor\n",
      "ok\n",
      "27  says  22 is a neighbor\n",
      "ok\n",
      "28 [38, 29, 27, 33, 35, 22, 26]\n",
      "28  says  38 is a neighbor\n",
      "ok\n",
      "28  says  29 is a neighbor\n",
      "ok\n",
      "28  says  27 is a neighbor\n",
      "ok\n",
      "28  says  33 is a neighbor\n",
      "ok\n",
      "28  says  35 is a neighbor\n",
      "ok\n",
      "28  says  22 is a neighbor\n",
      "ok\n",
      "28  says  26 is a neighbor\n",
      "ok\n",
      "29 [37, 30, 28, 25]\n",
      "29  says  37 is a neighbor\n",
      "ok\n",
      "29  says  30 is a neighbor\n",
      "ok\n",
      "29  says  28 is a neighbor\n",
      "ok\n",
      "29  says  25 is a neighbor\n",
      "ok\n",
      "30 [37, 29, 24, 21]\n",
      "30  says  37 is a neighbor\n",
      "ok\n",
      "30  says  29 is a neighbor\n",
      "ok\n",
      "30  says  24 is a neighbor\n",
      "ok\n",
      "30  says  21 is a neighbor\n",
      "ok\n",
      "31 [36, 34]\n",
      "31  says  36 is a neighbor\n",
      "ok\n",
      "31  says  34 is a neighbor\n",
      "ok\n",
      "32 [41, 40, 23, 20]\n",
      "32  says  41 is a neighbor\n",
      "ok\n",
      "32  says  40 is a neighbor\n",
      "ok\n",
      "32  says  23 is a neighbor\n",
      "ok\n",
      "32  says  20 is a neighbor\n",
      "ok\n",
      "33 [35, 20, 27, 28]\n",
      "33  says  35 is a neighbor\n",
      "ok\n",
      "33  says  20 is a neighbor\n",
      "ok\n",
      "33  says  27 is a neighbor\n",
      "ok\n",
      "33  says  28 is a neighbor\n",
      "ok\n",
      "34 [42, 36, 21, 31]\n",
      "34  says  42 is a neighbor\n",
      "ok\n",
      "34  says  36 is a neighbor\n",
      "ok\n",
      "34  says  21 is a neighbor\n",
      "ok\n",
      "34  says  31 is a neighbor\n",
      "ok\n",
      "35 [44, 38, 20, 33, 28]\n",
      "35  says  44 is a neighbor\n",
      "ok\n",
      "35  says  38 is a neighbor\n",
      "ok\n",
      "35  says  20 is a neighbor\n",
      "ok\n",
      "35  says  33 is a neighbor\n",
      "ok\n",
      "35  says  28 is a neighbor\n",
      "ok\n",
      "36 [46, 39, 34, 42, 31]\n",
      "36  says  46 is a neighbor\n",
      "ok\n",
      "36  says  39 is a neighbor\n",
      "ok\n",
      "36  says  34 is a neighbor\n",
      "ok\n",
      "36  says  42 is a neighbor\n",
      "ok\n",
      "36  says  31 is a neighbor\n",
      "ok\n",
      "37 [45, 38, 43, 29, 30]\n",
      "37  says  45 is a neighbor\n",
      "ok\n",
      "37  says  38 is a neighbor\n",
      "ok\n",
      "37  says  43 is a neighbor\n",
      "ok\n",
      "37  says  29 is a neighbor\n",
      "ok\n",
      "37  says  30 is a neighbor\n",
      "ok\n",
      "38 [43, 35, 28, 37]\n",
      "38  says  43 is a neighbor\n",
      "ok\n",
      "38  says  35 is a neighbor\n",
      "ok\n",
      "38  says  28 is a neighbor\n",
      "ok\n",
      "38  says  37 is a neighbor\n",
      "ok\n",
      "39 [46, 36]\n",
      "39  says  46 is a neighbor\n",
      "ok\n",
      "39  says  36 is a neighbor\n",
      "ok\n",
      "40 [47, 41, 32, 20]\n",
      "40  says  47 is a neighbor\n",
      "ok\n",
      "40  says  41 is a neighbor\n",
      "ok\n",
      "40  says  32 is a neighbor\n",
      "ok\n",
      "40  says  20 is a neighbor\n",
      "ok\n",
      "41 [47, 32, 40]\n",
      "41  says  47 is a neighbor\n",
      "ok\n",
      "41  says  32 is a neighbor\n",
      "ok\n",
      "41  says  40 is a neighbor\n",
      "ok\n",
      "42 [34, 36]\n",
      "42  says  34 is a neighbor\n",
      "ok\n",
      "42  says  36 is a neighbor\n",
      "ok\n",
      "43 [48, 45, 44, 38, 37]\n",
      "43  says  48 is a neighbor\n",
      "ok\n",
      "43  says  45 is a neighbor\n",
      "ok\n",
      "43  says  44 is a neighbor\n",
      "ok\n",
      "43  says  38 is a neighbor\n",
      "ok\n",
      "43  says  37 is a neighbor\n",
      "ok\n",
      "44 [49, 48, 35, 43]\n",
      "44  says  49 is a neighbor\n",
      "ok\n",
      "44  says  48 is a neighbor\n",
      "ok\n",
      "44  says  35 is a neighbor\n",
      "ok\n",
      "44  says  43 is a neighbor\n",
      "ok\n",
      "45 [48, 49, 37, 43]\n",
      "45  says  48 is a neighbor\n",
      "ok\n",
      "45  says  49 is a neighbor\n",
      "ok\n",
      "45  says  37 is a neighbor\n",
      "ok\n",
      "45  says  43 is a neighbor\n",
      "ok\n",
      "46 [36, 39]\n",
      "46  says  36 is a neighbor\n",
      "ok\n",
      "46  says  39 is a neighbor\n",
      "ok\n",
      "47 [40, 41]\n",
      "47  says  40 is a neighbor\n",
      "ok\n",
      "47  says  41 is a neighbor\n",
      "ok\n",
      "48 [49, 44, 43, 45]\n",
      "48  says  49 is a neighbor\n",
      "ok\n",
      "48  says  44 is a neighbor\n",
      "ok\n",
      "48  says  43 is a neighbor\n",
      "ok\n",
      "48  says  45 is a neighbor\n",
      "ok\n",
      "49 [44, 48, 45]\n",
      "49  says  44 is a neighbor\n",
      "ok\n",
      "49  says  48 is a neighbor\n",
      "ok\n",
      "49  says  45 is a neighbor\n",
      "ok\n"
     ]
    }
   ],
   "source": [
    "# Take a gal dictionary from 1 and test if there are any asymmetries.\n",
    "# An asymmetry occurs when i says j is a neighbor of i, but j does not say i is a neighbor of j.\n",
    "\n",
    "for key in gal_dict:\n",
    "    print(key, gal_dict[key])\n",
    "    for neighbor in gal_dict[key]:\n",
    "        print(key,' says ', neighbor, 'is a neighbor')\n",
    "        if key in gal_dict[neighbor]:\n",
    "            print('ok')\n",
    "        else:\n",
    "            print('not ok')\n",
    "            print('because ', neighbor, ' says that ', key, 'is not a neighbor')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
