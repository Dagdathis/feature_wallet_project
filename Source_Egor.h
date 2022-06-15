#pragma once
#include "Wallet.h"
#include "Transaction.h"

class Stock
{
	static int choice_1, choice_2;

public:
	static void allStock();
	static void userShares();
	static void totalValue();
	static void buy();
	static void sell();
	static void mainMenu(void);
	static void menu();
	static string selected_user;
};

