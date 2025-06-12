/*
1475번
 문제
다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

입력
첫째 줄에 다솜이의 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수이다.
 */
namespace Baekjoon_Array_1475
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string roomNum = Console.ReadLine();
            int numCnt = roomNum.Length;    // 방번호 글자 개수
            int needCnt = 0;
            List<int> list = new List<int>();
            List<int> initList = new List<int>
            {
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            };
            foreach (char c in roomNum)
            {
                list.Add(int.Parse(c.ToString()));
            }
            
            foreach (int i in list)
            {
                initList[i]++;
            }
            int sum69 = (initList[6] + initList[9] + 1) / 2;
            initList[6] = 0;
            initList[9] = 0;
            int maxCnt = initList.Max(x => x);
            int realMax = sum69 > maxCnt ? sum69 : maxCnt;
            needCnt = realMax;
            
            Console.WriteLine(needCnt);


        }
    }
}
