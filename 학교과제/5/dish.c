#include <stdio.h>

// 그릇의 높이를 계산하는 함수
int calculateHeight(char* arrangement, int num_dishes) {
    int height = 10; // 초기 높이 설정

    for (int i = 1; i < num_dishes; i++) {
        // 같은 방향으로 쌓이는 경우
        if (arrangement[i] == arrangement[i - 1]) {
            height += 5;
        }
        // 반대 방향으로 쌓이는 경우
        else {
            height += 10;
        }
    }

    return height;
}

int main() {
    FILE *input, *output;
    int num_cases;
    char arrangement[100];

    // 입력 파일 열기
    input = fopen("dish.inp", "r");
    if (input == NULL) {
        perror("Error opening input file");
        return -1;
    }

    // 출력 파일 열기
    output = fopen("dish.out", "w");
    if (output == NULL) {
        perror("Error opening output file");
        return -1;
    }

    // 총 경우의 수 입력 받기
    fscanf(input, "%d", &num_cases);

    // 각 테스트 케이스에 대해 계산하고 결과를 출력 파일에 쓰기
    for (int i = 0; i < num_cases; i++) {
        int num_dishes;
        // 그릇의 개수와 모양 입력 받기
        fscanf(input, "%d %s", &num_dishes, arrangement);

        // 그릇의 높이 계산
        int height = calculateHeight(arrangement, num_dishes);

        // 결과 출력
        fprintf(output, "%d\n", height);
    }

    // 파일 닫기
    fclose(input);
    fclose(output);

    return 0;
}
