#include <iostream>
#include <string>
#include <vector>

int solution(std::string my_string, std::string is_prefix) {
    int stack = 0;

    if (my_string.length() < is_prefix.length())
        return 0;


    for (int i = 0; i < is_prefix.length(); i++)
        if (my_string[i] != is_prefix[i])
            return 0;

    return 1;
}

int main()
{
    std::string my_string = "banana";
    std::cout << solution(my_string, "ban") << std::endl;
    std::cout << solution(my_string, "nan") << std::endl;
    std::cout << solution(my_string, "abcd") << std::endl;
    std::cout << solution(my_string, "bananan") << std::endl;
    return 0;
}