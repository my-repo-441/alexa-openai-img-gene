from openai import OpenAI
import requests

client = OpenAI()

#漫画のページ数
n_pages = 6

#漫画の設定
world_building = "Far in the future, space has become a new frontier for mankind. People lived on numerous stars and built a space society where different cultures and technologies intersected. However, unknown dangers lurk in the vastness of space, and many threaten the peace. The Guardians of Starlight who protect each star system, play an active role."

# 指定されたページ数だけ画像生成を繰り返す
for i in range(1, n_pages + 1):

  if i==1:
    response_img = client.images.generate(
      model="dall-e-3",
      prompt = f"This is first frame of a {n_pages}-page shonen battle manga. Draw the first frame. World building is as follows:'{world_building}'",
      size="1024x1024",
      quality="standard",
      n=1,
    )

    image_url = response_img.data[0].url
    print(image_url)

    # 画像をダウンロードするためのリクエストを送信
    response = requests.get(image_url)

    # リクエストが成功した場合（HTTPステータスコード200）
    if response.status_code == 200:
        # バイナリモードで画像ファイルを開き、内容を書き込む
        with open(f"downloaded_image{i}.png", "wb") as file:
            file.write(response.content)
        print("Image successfully downloaded and saved.")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

  elif i == n_pages:
    response_vision = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "What’s in this image?"},
          {
            "type": "image_url",
            "image_url": {
              "url": image_url,
            },
          },
        ],
      }
    ],
    max_tokens=300,
  )

    # 結果の 'content' のみを出力
    print(response_vision.choices[0].message.content)
    prompt = response_vision

    response_img = client.images.generate(
      model="dall-e-3",
      prompt = f"This is the final frame of a {n_pages}-page shonen battle manga. Draw a continuation of the previous page. The previous page situation are as follows:'{prompt}' World building is as follows:'{world_building}'",
      size="1024x1024",
      quality="standard",
      n=1,
    )

    image_url = response_img.data[0].url
    print(image_url)
    print("fin.")
    
    # 画像をダウンロードするためのリクエストを送信
    response = requests.get(image_url)

    # リクエストが成功した場合（HTTPステータスコード200）
    if response.status_code == 200:
        # バイナリモードで画像ファイルを開き、内容を書き込む
        with open(f"downloaded_image{i}.png", "wb") as file:
            file.write(response.content)
        print("Image successfully downloaded and saved.")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")


  else:
    response_vision = client.chat.completions.create(
      model="gpt-4-vision-preview",
      messages=[
        {
          "role": "user",
          "content": [
            {"type": "text", "text": "What’s in this image?"},
            {
              "type": "image_url",
              "image_url": {
                "url": image_url,
              },
            },
          ],
        }
      ],
      max_tokens=300,
    )

    # 結果の 'content' のみを出力
    print(response_vision.choices[0].message.content)
    prompt = response_vision


    response_img = client.images.generate(
      model="dall-e-3",
        prompt = f"This is {i} frame of a {n_pages}-page shonen battle manga. Draw a continuation of the previous page. The previous page situation are as follows:'{prompt}' World building is as follows:'{world_building}'",
      size="1024x1024",
      quality="standard",
      n=1,
    )

    image_url = response_img.data[0].url
    print(image_url)

        # 画像をダウンロードするためのリクエストを送信
    response = requests.get(image_url)

    # リクエストが成功した場合（HTTPステータスコード200）
    if response.status_code == 200:
        # バイナリモードで画像ファイルを開き、内容を書き込む
        with open(f"downloaded_image{i}.png", "wb") as file:
            file.write(response.content)
        print("Image successfully downloaded and saved.")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

