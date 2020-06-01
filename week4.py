{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Lesson4/3.27.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNeXtQVgdbwtw/euB3pgToA",
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
        "<a href=\"https://colab.research.google.com/github/lile55555/computational-thinkin-and-program-design/blob/master/week4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wOfP9pMZ1I1y",
        "colab_type": "text"
      },
      "source": [
        " 3/27 資料科學概論 (運算符號)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Z-MhqRYUrZBx",
        "colab_type": "code",
        "outputId": "7add9e72-72c8-4b1f-cd40-c5055290a700",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        " #華氏換算攝氏\n",
        "current_celsius = 28\n",
        "current_fahrenheit = current_celsius * 9 / 5 + 32\n",
        "print(current_fahrenheit)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "82.4\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "R2jqI-H4wfJq",
        "colab_type": "code",
        "outputId": "4e664547-84ef-445e-b529-99735fc16f69",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        " #籃球球星BMI\n",
        "shaq_height = 216\n",
        "shaq_weight = 147\n",
        "shaq_bmi = shaq_weight / (shaq_height/100)**2\n",
        "print(shaq_bmi)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "31.507201646090532\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JKDtXqmOzNJL",
        "colab_type": "code",
        "outputId": "dfc842f5-e628-48c2-aa94-3c49f89826ea",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        " #本人BMI測量\n",
        "lily_height = 166\n",
        "lily_weight = 68\n",
        "lily_bmi = lily_weight / (lily_height/100)**2\n",
        "print(lily_bmi)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "24.677021338365513\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vsCJZNlCzwih",
        "colab_type": "code",
        "outputId": "0d6e785b-db30-42f8-a5e7-5a67d0edd21c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "source": [
        " #單雙引號建立文字,不會有分別\n",
        "movie_title = \"陽光普照\"\n",
        "print(movie_title)\n",
        "print(type(movie_title))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "陽光普照\n",
            "<class 'str'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "liNC14oV156b",
        "colab_type": "code",
        "outputId": "461b2a40-5332-4d03-9aa0-e0e288a4e6b4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 131
        }
      },
      "source": [
        " #單引號容易造成無法印出外國人名\n",
        "shaq ='shaquille O'Neal'"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-16-0c2893f2f747>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    shaq ='shaquille O'Neal'\u001b[0m\n\u001b[0m                          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "figADR8r2TAk",
        "colab_type": "code",
        "outputId": "036a843a-ff7d-4a86-92c3-97a3d8a61640",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "source": [
        " #使用反斜線\\跳脫字元\n",
        "shaq = 'shaquille O\\'Neal'\n",
        "print(shaq)\n",
        "print(type(shaq))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "shaquille O'Neal\n",
            "<class 'str'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EPKYtZ9u2szJ",
        "colab_type": "code",
        "outputId": "3b00c52a-6f56-48d7-e5be-6b23082e19f9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "source": [
        " #隨堂練習 使用\\隔開單引號和字元\n",
        "lvi = 'i\\'m  lovein\\' it!'\n",
        "print(lvi)\n",
        "print(type(lvi))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "i'm  lovein' it!\n",
            "<class 'str'>\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "XT3kc7eC3gYb",
        "colab_type": "code",
        "outputId": "eb97b956-f52d-4943-e28d-a5681ef0bb88",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        " #隨堂練習 What did Ross say\n",
        "ross_said = \"\"\"Let's put aside the fact that you \"accidentally\" pick up my grandmother's ring.\"\"\"\n",
        "print(ross_said)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Let's put aside the fact that you \"accidentally\" pick up my grandmother's ring.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lZlC71aM-8rs",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        " #印出 陽光普照的評等是7.7，片長為156分鐘\n",
        "movie_title = \"陽光普照\"\n",
        "movie_rating = 7.7\n",
        "movie_time = 156"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vKuE0E4h60OT",
        "colab_type": "code",
        "outputId": "79a7d708-bd1d-4cbc-a0b5-800ae2de5f01",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        " #在文字裡頭遷入物件的值\n",
        "\"{}的評等是{}，片長為{}分鐘\".format(movie_title, movie_rating, movie_time)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'陽光普照的評等是7.7，片長為156分鐘'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 47
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JQlctbzb_SeF",
        "colab_type": "code",
        "outputId": "6580cf8f-156e-47ba-aafa-5e8f52c2492c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "source": [
        " #使用input設一個提示\n",
        "movie_title = input(\"請輸入電影的名稱\")\n",
        "movie_rating = input(\"請輸入電影的評等\")"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "請輸入電影的名稱Call me by your name\n",
            "請輸入電影的評等8.5\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cZlHuZdfBSbk",
        "colab_type": "code",
        "outputId": "8f135fd6-59dc-4fab-ce44-8b170703a95e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "source": [
        " #印出電影名稱跟評等\n",
        "print(movie_title)\n",
        "print(movie_rating)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Call me by your name\n",
            "8.5\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ga941ntXCfV4",
        "colab_type": "code",
        "outputId": "79e1f0dc-04ca-4bcd-cb59-ca9e6d9c2040",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "source": [
        " #隨堂練習 -我在00,天氣00-\n",
        "city_title = input(\"我在\")\n",
        "city_weather = input(\"天氣\")"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "我在Yuli\n",
            "天氣sunny\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UeKEZ1V3Cvvu",
        "colab_type": "code",
        "outputId": "6ec266e5-3d04-43b8-d765-40c9c893419a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        " #使用.format(物件,物件) 嵌入\n",
        "print(\"我在{}，天氣{}\".format(city_title,city_weather))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "我在Yuli，天氣sunny\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MPRwjiNnEEYY",
        "colab_type": "code",
        "outputId": "fb0a3d06-506d-4b81-a482-9ae012037456",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        }
      },
      "source": [
        " #用加號嵌入 /不太建議 會有問題\n",
        "city = input(\"i'm in\")\n",
        "weather = input (\",weathe is\")\n",
        "print(\"i'm in\"+city+\",weather is\"+weather)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "i'm in Tokyo\n",
            ",weathe is cloudy\n",
            "i'm in Tokyo,weather is cloudy\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QDmuiRF3FIN2",
        "colab_type": "code",
        "outputId": "317cbb76-ad06-4d0a-a88c-baff011cc16a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "print(\"哈哈\"*5)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "哈哈哈哈哈哈哈哈哈哈\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3KsdHjCVGrfd",
        "colab_type": "code",
        "outputId": "90737dd6-b8ec-4ad1-eaa6-cfdc5b967ece",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 51
        }
      },
      "source": [
        " #布林 Ture False 要大寫\n",
        "print(True)\n",
        "print(False) "
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "True\n",
            "False\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GR3vQas3HeZo",
        "colab_type": "code",
        "outputId": "f3939ca6-d2c8-4651-da98-ad4d520e6e42",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "movie_rating = 7.7\n",
        "print(movie_rating > 8)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "False\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QeU_oAABIl7J",
        "colab_type": "code",
        "outputId": "e2685ea4-e209-4354-c6c7-c531d565191d",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        " #隨堂練習 身分證字號尾數是否奇數 ==1 \n",
        " #用餘數判斷 %\n",
        "id_last_digit = 6\n",
        "id_last_digit % 6 ==1"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "False"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 52
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4G6psLNYJRwx",
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