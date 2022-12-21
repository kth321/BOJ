#include <stdio.h>

int main()
{
	int n;
	int num[10001] = { 0 };

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		int tmp;
		scanf("%d", &tmp);
		num[tmp]++;
	}
	for (int i = 0; i < 10001; i++)
	{
		if (num[i] != 0)
			for (int j = 0; j < num[i]; j++)
				printf("%d\n", i);
	}
	return 0;
}