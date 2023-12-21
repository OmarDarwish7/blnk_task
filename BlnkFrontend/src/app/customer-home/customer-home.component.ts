import { Component, OnInit } from '@angular/core';
import { WebService } from '../web.service';

@Component({
  selector: 'app-customer-home',
  templateUrl: './customer-home.component.html',
  styleUrls: ['./customer-home.component.css']
})
export class CustomerHomeComponent implements OnInit {

  loanSchemas:any=[];
  userLoans:any = [];
  selectedLoanSchema :any;
  loanAmount: number=0;
  currentUser:any
  users = [
    {id: 1, name: "Test",email:"aaa"}
  ]

  constructor(
    private webService: WebService
  ) { }

  ngOnInit(): void {
    this.currentUser = JSON.parse(sessionStorage.getItem('currentuser')!);
    this.fetchLoanSchemas();
    this.fetchUserLoans();
  }

  fetchLoanSchemas(): void {
    this.webService.get(
      'loan_schema/get_all_loan_schemas/'
    ).subscribe((response)=>{
      const object:any = response
      this.loanSchemas = object.loan_schemas;
      console.log(response)
    });
  }

  fetchUserLoans(): void {
    this.webService.post(
      'loan/get_customer_loans/',
      {id: this.currentUser.id}
    ).subscribe((response)=>{
      const object:any=response;
      this.userLoans = object.data;
      console.log(response)
    })
  }

  applyForLoan() {
    if (this.loanAmount> 0) {
      console.log("Sending")
      this.webService.post(
        'loan/add_loan/',
        {customer : this.currentUser.id, amount : this.loanAmount}
      ).subscribe((response)=>{
        console.log(response);
        window.location.reload();
      })
    }
  }

  payInstallment(loanId:any) {
    console.log({
      loan_id:loanId,
      customer_id:this.currentUser.id
    })
    this.webService.post(
      'loan/pay_installment/',
      {
        loan_id:loanId,
        customer_id:this.currentUser.id
      }
    ).subscribe((response)=>{
      console.log(response)
      window.location.reload();
    })
  }

}
