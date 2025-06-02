// 입력받은 정수의 소수 개수 구하기
namespace Prime_Number_Count
{
    internal class PrimeNumberCount
    {
        static void Main(string[] args)
        {
            // Input
            var count = 0;
            var sw = true;  // 소수(true) 소수가 아니면(false) 확인하는 스위치 변수(flag)
            var number = 0;
            Console.Write("수 입력 : _\b");
            number = Convert.ToInt32(Console.ReadLine());

            // Process
            for (int i = 2; i <= number; i++)
            {
                sw = true;
                for (int j = 2; j < i; j++)
                {
                    if (i % j == 0)
                    {
                        sw = false;
                        break;
                    }
                }
                if (sw)
                {
                    Console.Write(i + "\t");
                    count++;

                    if (count % 5 == 0)
                    {
                        Console.WriteLine();
                    }
                }
            }
            Console.WriteLine();

            // Output
            Console.WriteLine(count + "개");
        }
    }
}
