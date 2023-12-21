import { Component, OnInit } from '@angular/core';
import { WebService } from '../web.service';
@Component({
  selector: 'app-personnel-home',
  templateUrl: './personnel-home.component.html',
  styleUrls: ['./personnel-home.component.css']
})
export class PersonnelHomeComponent implements OnInit {

  min_amount!:number;
  max_amount!:number;
  interest_rate!:number;
  term!:number;
  bank_percentage!:number;
  currentBudget:number=0.0
  loanSchemas:any[]=[]
  loans:any[]=[]


  constructor(
    private webService : WebService
  ) {}

  ngOnInit(): void {
    this.webService.get(
      'loan/get_all_loans/'
    ).subscribe((response)=>{
      const object:any = response;
      this.loans = object.loans;
    })
    this.getCurrentBudget();
    this.fetchLoanSchemas();
  }

  getCurrentBudget(){
    this.webService.get(
      'loan_provider/get_current_budget/'
    ).subscribe((response:any)=>{
      console.log(response);
      this.currentBudget = response.budget;
    })
  }



  submitLoanSchema() {
    console.log('IN')
    if(this.min_amount >=0 && this.max_amount && this.interest_rate && this.term && this.bank_percentage){
      console.log("IN IN");
      this.webService.post(
        'loan_schema/add_loan_schema/',
        {
          min_amount:this.min_amount,
          max_amount: this.max_amount,
          interest_rate: this.interest_rate,
          term: this.term,
          bank_percentage: this.bank_percentage
        }
      ).subscribe((response)=>{
        console.log(response)
        window.location.reload();
      })
    }
  }

  acceptLoan(loanId:number){
    this.webService.post(
      'loan/accept_loan/',
      {id: loanId}
    ).subscribe((response)=>{
      console.log(response);
    })
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

}
