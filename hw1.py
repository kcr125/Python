{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8eb55e09-bfeb-412c-9914-2bca33450174",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "넓이를 구하고자 하는 원의 반지름은? 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "반지름 4 인 원의 넓이 = 3.14 x 4 x 4 = 50.24\n"
     ]
    }
   ],
   "source": [
    "def get_radius(prompt):\n",
    "    r = int(input(prompt))\n",
    "    return r\n",
    "\n",
    "def get_circle_area(r) :\n",
    "    area=3.14*(r**2)\n",
    "    return area\n",
    "\n",
    "r=get_radius('넓이를 구하고자 하는 원의 반지름은?')\n",
    "result=get_circle_area(r)\n",
    "\n",
    "area=get_circle_area(r)\n",
    "print('반지름', r, '인 원의 넓이 = 3.14 x', r, 'x', r, '=', area)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4b4fdffb-b0b7-4f73-bae3-408043d97aa8",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
