# GiGS-eBook
a python library to search free eBooks online using [Library Genesis](https://en.wikipedia.org/wiki/Library_Genesis)'s database

# Installation
`pip3 install gigsebook`

# TODO
* Better error handling

# USAGE
* import the class FetchData

    `from gigsebook import FetchData`
* initialize an instance of `FetchData` with the query

    `output = FetchData('your_query')`
* now `output.data` should be filled with the returned info, use it to your needs. e.g.

    `print(output.data)`

    should provide you with:

    ```
    [
        {
            'title': 'dummy',
            'author': 'dummy, dummy2',
            'year': '0000',
            'publication': 'dummy',
            'pages': '0',
            'language': 'dummy',
            'size': '0 Bytes',
            'extention': 'none',
            'links': ['https://example.example',
                      'https://example2.example']
        },

        {
            'title': 'dummy',
            'author': 'dummy, dummy2',
            'year': '0000',
            'publication': 'dummy',
            'pages': '0',
            'language': 'dummy',
            'size': '0 Bytes',
            'extention': 'none',
            'links': ['https://example.example',
                      'https://example2.example']
        },

        .
        .
        .
    ]
    ```

    *Note that the output above is not JSON, It's just a list of dictionaries. The representation is just to make it readable.*


# NOTES
**I DO NOT RECOMMEND PIRACY OF ANY CREATION, BUY THE ORIGINAL COPIES TO SUPPORT THE AUTHOR. THIS CODE IS FOR EDUCATIONAL PURPOSES. FOR OTHER USES, YOU ARE RESPONSIBLE FOR WHAT YOU DO.**

# LICENSE
Licensed under MIT License

*Copyright (c) 2020 Gaurav Kumar Yadav*

Head over to the `LICENSE` for details