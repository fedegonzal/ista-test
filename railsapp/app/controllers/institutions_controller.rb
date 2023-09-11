class InstitutionsController < ApplicationController
  def index
    params[:col] ||= "id"
    params[:dir] ||= "asc"
    @institutions = Institution.all(params[:col], params[:dir])


    # I'm sure that there is a better way to do this :)
    @sorting = { 
      id: "",
      university: "",
      country: "",
    }
    @sorting[params[:col].to_sym] = params[:dir] == "asc" ? "asc" : "desc"

    @action = { 
      id: "asc",
      university: "asc",
      country: "asc",
    }
    @action[params[:col].to_sym] = params[:dir] == "asc" ? "desc" : "asc"

  end
end
