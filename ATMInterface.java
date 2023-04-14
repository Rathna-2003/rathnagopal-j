import java.util.Scanner;

public class ATMInterface {
    private static Scanner scanner = new Scanner(System.in);
    private static double balance = 5000.0; // initial balance
    private static String transactionHistory = ""; // to store transaction history

    public static void main(String[] args) {
        int choice = 0;
        do {
            System.out.println("ATM Interface\n");
            System.out.println("1. View Balance");
            System.out.println("2. Withdraw");
            System.out.println("3. Money Transfer");
            System.out.println("4. Transaction History");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");

            choice = scanner.nextInt();
            switch (choice) {
                case 1:
                    viewBalance();
                    break;
                case 2:
                    withdraw();
                    break;
                case 3:
                    moneyTransfer();
                    break;
                case 4:
                    viewTransactionHistory();
                    break;
                case 5:
                    System.out.println("Thank you for using the ATM Interface!");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.\n");
                    break;
            }
        } while (choice != 5);
    }

    private static void viewBalance() {
        System.out.printf("Your current balance is $%.2f\n\n", balance);
    }

    private static void withdraw() {
        System.out.print("Enter the amount you want to withdraw: ");
        double amount = scanner.nextDouble();

        if (amount > balance) {
            System.out.println("Insufficient balance. Please try again.\n");
            return;
        }

        balance -= amount;
        transactionHistory += String.format("Withdrawal of $%.2f\n", amount);

        System.out.printf("Withdrawal successful. Your current balance is $%.2f\n\n", balance);
    }

    private static void moneyTransfer() {
        System.out.print("Enter the amount you want to transfer: ");
        double amount = scanner.nextDouble();

        if (amount > balance) {
            System.out.println("Insufficient balance. Please try again.\n");
            return;
        }

        System.out.print("Enter the recipient's account number: ");
        String accountNumber = scanner.next();

        // validate the recipient's account number
        // if it's valid, transfer the money and update the transaction history
        // if it's invalid, show an error message and return

        balance -= amount;
        transactionHistory += String.format("Money transfer of $%.2f to account %s\n", amount, accountNumber);

        System.out.printf("Money transfer successful. Your current balance is $%.2f\n\n", balance);
    }

    private static void viewTransactionHistory() {
        System.out.println("Transaction History\n");
        System.out.println(transactionHistory);
    }
}