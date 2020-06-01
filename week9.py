{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled7.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMHxnmzFAu0Y/r6oWwDd6LK",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/lile55555/computational-thinkin-and-program-design/blob/master/5/1%20class.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hsRJb_v3DMmt",
        "colab_type": "text"
      },
      "source": [
        "#Python visualize 網址\n",
        "http://www.pythontutor.com/visualize.html#mode=display"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qZcI5uzCBNSZ",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 153
        },
        "outputId": "8fae90ce-a041-49da-ce83-8272fcc3a7cc"
      },
      "source": [
        "x = int(input(\"請輸入起始的整數:\")) #start\n",
        "y = int(input(\"請輸入終止的整數:\")) #stop\n",
        "i = x\n",
        "while i <= y: #stop\n",
        "#task\n",
        "  print(i) \n",
        "  i += 1 #step"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入起始的整數:5\n",
            "請輸入終止的整數:10\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n",
            "10\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "A1P6uXrFCKS8",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 102
        },
        "outputId": "1e189795-5034-4744-9674-7aa2dd8120ee"
      },
      "source": [
        "#隨堂練習 5-10印出基數\n",
        "x = int(input(\"請輸入起始的整數:\")) #start\n",
        "y = int(input(\"請輸入終止的整數:\")) #stop\n",
        "i = x #start\n",
        "while i <= y: #stop\n",
        "  #task\n",
        "  if i % 2 == 1: #基數\n",
        "    print(i) #歸屬於if\n",
        "  i += 1 #step #歸屬於while迴圈"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入起始的整數:5\n",
            "請輸入終止的整數:10\n",
            "5\n",
            "7\n",
            "9\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xc09NCElETXU",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        },
        "outputId": "8131dce5-d5bd-4aef-b2d7-357eb578a870"
      },
      "source": [
        "x = int(input(\"請輸入起始的整數:\")) \n",
        "y = int(input(\"請輸入終止的整數:\")) \n",
        "odd_counter = 0 #歸零\n",
        "i = x #start\n",
        "while i <= y: #stop\n",
        "  #task\n",
        "  if i % 2 == 1:\n",
        "    #odd_counter = odd_counter + 1 # = NOT == 單等號(宣告) 雙等號(等於)\n",
        "    odd_counter += 1 #技術累計\n",
        "  i += 1 #step\n",
        "print(odd_counter)"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入起始的整數:5\n",
            "請輸入終止的整數:10\n",
            "3\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3CKUD7EgGAn_",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 85
        },
        "outputId": "6d4f35f1-f2f8-4a84-f9fb-f12ed174c1af"
      },
      "source": [
        "x = int(input(\"請輸入起始的整數:\")) \n",
        "y = int(input(\"請輸入終止的整數:\")) \n",
        "odd_summation = 0 #歸零\n",
        "i = x #start\n",
        "while i <= y: #stop\n",
        "    #task\n",
        "  if i % 2 == 1:\n",
        "     odd_summation = odd_summation + i  #數值累加\n",
        "  i += 1 #step\n",
        "print(\"======\")\n",
        "print(odd_summation)"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入起始的整數:5\n",
            "請輸入終止的整數:10\n",
            "======\n",
            "21\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jotSlA6hHuZj",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        },
        "outputId": "4d3b4bcf-5d7b-49c6-be4c-f4ebd62dd590"
      },
      "source": [
        "x = int(input(\"請輸入起始的整數:\")) \n",
        "y = int(input(\"請輸入終止的整數:\")) \n",
        "odd_summation = 0 #歸零\n",
        "odd_counter = 0\n",
        "i = x #start\n",
        "while i <= y: #stop\n",
        "   #task\n",
        "   if i % 2 == 1:\n",
        "        odd_counter += 1 #計數累計\n",
        "        odd_summation += i  #數值累加\n",
        "        print(\"現在的整數是:{},奇數計數為{}個,總和為{}\" .format(i, odd_counter, odd_summation))\n",
        "   else:\n",
        "        print(\"現在的整數是:{},奇數計數為{}個,總和為{}\" .format(i, odd_counter, odd_summation))\n",
        "   i += 1 #step\n",
        "print(\"======\")\n",
        "print(odd_counter)\n",
        "print(odd_summation)"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入起始的整數:5\n",
            "請輸入終止的整數:10\n",
            "現在的整數是:5,奇數計數為1個,總和為5\n",
            "現在的整數是:6,奇數計數為1個,總和為5\n",
            "現在的整數是:7,奇數計數為2個,總和為12\n",
            "現在的整數是:8,奇數計數為2個,總和為12\n",
            "現在的整數是:9,奇數計數為3個,總和為21\n",
            "現在的整數是:10,奇數計數為3個,總和為21\n",
            "======\n",
            "3\n",
            "21\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yhOvnklIJ13C",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 238
        },
        "outputId": "e25abde4-88ea-4d90-83d6-ac7f3a709bb2"
      },
      "source": [
        "#因數分解\n",
        "x = int(input(\"請輸入一個正整數:\"))\n",
        "i = 1 #start\n",
        "divisor_counter = 0 #歸零\n",
        "while i <= x: #stop\n",
        "   if x % i ==0:\n",
        "     print(\"{}可以被{}整除\" . format(x, i))\n",
        "     print(\"因數個數目前有{}個\" . format(divisor_counter))\n",
        "     print(\"---------\")\n",
        "   i += 1 #step"
      ],
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入一個正整數:55\n",
            "55可以被1整除\n",
            "因數個數目前有0個\n",
            "---------\n",
            "55可以被5整除\n",
            "因數個數目前有0個\n",
            "---------\n",
            "55可以被11整除\n",
            "因數個數目前有0個\n",
            "---------\n",
            "55可以被55整除\n",
            "因數個數目前有0個\n",
            "---------\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PAk65S5nNJ7p",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 340
        },
        "outputId": "27d21673-f749-4e3c-98ef-9fb3c72ac02f"
      },
      "source": [
        "# 因數分解後判斷質數\n",
        "x = int(input(\"請輸入一個正整數:\"))\n",
        "i = 1 #start\n",
        "divisor_counter = 0 #歸零\n",
        "while i <= x: #stop\n",
        "   if x % i ==0:\n",
        "     divisor_counter += 1\n",
        "     print(\"{}可以被{}整除\" . format(x, i))\n",
        "     print(\"因數個數目前有{}個\" . format(divisor_counter))\n",
        "     print(\"--------\")\n",
        "   i += 1 #step\n",
        "print(\"### Answer ###\")\n",
        "print(\"{}共有{}個因數!\" .format(x, divisor_counter))\n",
        "if divisor_counter ==2:\n",
        "  print(\"{}是質數\" .format(x))\n",
        "else:\n",
        "  print(\"{}不是質數\" .format(x))"
      ],
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入一個正整數:16\n",
            "16可以被1整除\n",
            "因數個數目前有1個\n",
            "--------\n",
            "16可以被2整除\n",
            "因數個數目前有2個\n",
            "--------\n",
            "16可以被4整除\n",
            "因數個數目前有3個\n",
            "--------\n",
            "16可以被8整除\n",
            "因數個數目前有4個\n",
            "--------\n",
            "16可以被16整除\n",
            "因數個數目前有5個\n",
            "--------\n",
            "### Answer ###\n",
            "16共有5個因數!\n",
            "16不是質數\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ieIMhJwRR3pd",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 357
        },
        "outputId": "cd82b145-592b-410c-b8aa-ffb6bf33ca74"
      },
      "source": [
        "x = int(input(\"請輸入一個正整數:\"))\n",
        "i = 1 #start\n",
        "divisor_counter = 0 #歸零\n",
        "while i <= x: #stop\n",
        "   if x % i ==0:\n",
        "     divisor_counter += 1\n",
        "     print(\"{}可以被{}整除\" . format(x, i))\n",
        "     print(\"因數個數目前有{}個\" . format(divisor_counter))\n",
        "     print(\"--------\")\n",
        "   i += 1 #step\n",
        "print(\"### Answer ###\")\n",
        "print(\"總共執行{}次迴圈\" .format(x))\n",
        "print(\"{}共有{}個因數!\" .format(x, divisor_counter))\n",
        "if divisor_counter ==2:\n",
        "  print(\"{}是質數\" .format(x))\n",
        "else:\n",
        "  print(\"{}不是質數\" .format(x))"
      ],
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入一個正整數:16\n",
            "16可以被1整除\n",
            "因數個數目前有1個\n",
            "--------\n",
            "16可以被2整除\n",
            "因數個數目前有2個\n",
            "--------\n",
            "16可以被4整除\n",
            "因數個數目前有3個\n",
            "--------\n",
            "16可以被8整除\n",
            "因數個數目前有4個\n",
            "--------\n",
            "16可以被16整除\n",
            "因數個數目前有5個\n",
            "--------\n",
            "### Answer ###\n",
            "總共執行16次迴圈\n",
            "16共有5個因數!\n",
            "16不是質數\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_Pv2lcc5VZjG",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 238
        },
        "outputId": "40f91b04-25f0-4242-ff06-3ed77d601f8c"
      },
      "source": [
        "#寫入break讓運算更快\n",
        "x = int(input(\"請輸入一個正整數:\"))\n",
        "i = 1 #start\n",
        "divisor_counter = 0 #歸零\n",
        "while i <= x: #stop\n",
        "   if x % i ==0:\n",
        "     divisor_counter += 1\n",
        "     print(\"{}可以被{}整除\" . format(x, i))\n",
        "     print(\"因數個數目前有{}個\" . format(divisor_counter))\n",
        "     print(\"--------\")\n",
        "   i += 1 #step \n",
        "   if divisor_counter >2:\n",
        "     break\n",
        "print(\"### Answer ###\")\n",
        "print(\"總共執行{}次迴圈\" .format(i - 1))\n",
        "if divisor_counter ==2:\n",
        "  print(\"{}是質數\" .format(x))\n",
        "else:\n",
        "  print(\"{}不是質數\" .format(x))"
      ],
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入一個正整數:50\n",
            "50可以被1整除\n",
            "因數個數目前有1個\n",
            "--------\n",
            "50可以被2整除\n",
            "因數個數目前有2個\n",
            "--------\n",
            "50可以被5整除\n",
            "因數個數目前有3個\n",
            "--------\n",
            "### Answer ###\n",
            "總共執行5次迴圈\n",
            "50不是質數\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "D791kXpbWEGa",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "#continue 略過某次作業"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "N48uzu1pXGgg",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "outputId": "4f0f9fbe-d7a5-46c8-d17e-35b244a36dec"
      },
      "source": [
        "i = 1\n",
        "while i <= 100:\n",
        "  if i % 15 ==0:\n",
        "    print(\"Fizz Buzz\")\n",
        "  elif i % 3 ==0:\n",
        "    print(\"Fizz\") \n",
        "  elif i % 5 ==0:\n",
        "    print(\"Buzz\")\n",
        "  else: \n",
        "    print(i)\n",
        "  i += 1"
      ],
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1\n",
            "2\n",
            "Fizz\n",
            "4\n",
            "Buzz\n",
            "Fizz\n",
            "7\n",
            "8\n",
            "Fizz\n",
            "Buzz\n",
            "11\n",
            "Fizz\n",
            "13\n",
            "14\n",
            "Fizz Buzz\n",
            "16\n",
            "17\n",
            "Fizz\n",
            "19\n",
            "Buzz\n",
            "Fizz\n",
            "22\n",
            "23\n",
            "Fizz\n",
            "Buzz\n",
            "26\n",
            "Fizz\n",
            "28\n",
            "29\n",
            "Fizz Buzz\n",
            "31\n",
            "32\n",
            "Fizz\n",
            "34\n",
            "Buzz\n",
            "Fizz\n",
            "37\n",
            "38\n",
            "Fizz\n",
            "Buzz\n",
            "41\n",
            "Fizz\n",
            "43\n",
            "44\n",
            "Fizz Buzz\n",
            "46\n",
            "47\n",
            "Fizz\n",
            "49\n",
            "Buzz\n",
            "Fizz\n",
            "52\n",
            "53\n",
            "Fizz\n",
            "Buzz\n",
            "56\n",
            "Fizz\n",
            "58\n",
            "59\n",
            "Fizz Buzz\n",
            "61\n",
            "62\n",
            "Fizz\n",
            "64\n",
            "Buzz\n",
            "Fizz\n",
            "67\n",
            "68\n",
            "Fizz\n",
            "Buzz\n",
            "71\n",
            "Fizz\n",
            "73\n",
            "74\n",
            "Fizz Buzz\n",
            "76\n",
            "77\n",
            "Fizz\n",
            "79\n",
            "Buzz\n",
            "Fizz\n",
            "82\n",
            "83\n",
            "Fizz\n",
            "Buzz\n",
            "86\n",
            "Fizz\n",
            "88\n",
            "89\n",
            "Fizz Buzz\n",
            "91\n",
            "92\n",
            "Fizz\n",
            "94\n",
            "Buzz\n",
            "Fizz\n",
            "97\n",
            "98\n",
            "Fizz\n",
            "Buzz\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OqpI6NgLZjXs",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}
