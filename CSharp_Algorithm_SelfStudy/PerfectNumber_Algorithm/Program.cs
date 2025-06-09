// 완전수 : 자신을 제외한 약수의 합이 자신과 같은 수
// ex) 6 = 1 + 2 + 3
// 1부터 10000까지의 완전수와 개수 출력
namespace Perfect_Number_Algorithm
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int sum = 0;    // 약수 합계
            int count = 0;  // 완전수 개수
            int max = 0;    // 가장 큰 약수
            int rem = 0;    // 나머지값

            for (int i = 1; i <= 10000; i++)
            {
                sum = 0;    // 매 반복마다 0으로 초기화
                max = i / 2;    // 모든 짝수를 2로 나누면 가장 큰 약수 구할 수 있음
                for (int j = 1; j <= max; j++)
                {
                    rem = i % j;    // 자신 나누기 약수
                    if (rem == 0)
                    {
                        sum += j;   // 약수 합계
                    }
                }
                if (i == sum)   // 자신과 약수의 합계 같으면
                {
                    Console.WriteLine($"완전수 : {i}");
                    count++;
                }
            }

            Console.WriteLine($"완전수 개수 : {count}");
        }
    }
}
