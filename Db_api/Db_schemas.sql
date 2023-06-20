create table companies(
    company_id int not null,
    company_name varchar(255) not null,
    company_city varchar(255),
    company_state varchar(255),
    company_email varchar(255),
    created_by_user int,
    _created_at timestamp not null,
    _updated_at timestamp not null,
    primary key(company_id),
    foreign key (created_by_user) references users(user_id)
);

create table users(
    user_id int not null,
    user_email varchar(255) not null,
    user_password varchar(255) not null,
    user_name varchar(255) not null,
    user_adm boolean, --Admin, sys_user
    user_type varchar(255), --Single user or company user
    _created_at timestamp not null,
    _updated_at timestamp not null,
    primary key(user_id),
);

create table projects(
    project_id int not null,
    project_name varchar(255) not null,
    project_owner int not null,
    project_deadline date,
    _created_at timestamp not null,
    _updated_at timestamp not null,
    primary key(project_id),
    foreign key (project_owner) references users(user_id)
);

create table tasks(
    task_id int not null,
    task_name varchar(255) not null,
    task_project int not null,
    task_user int not null,
    task_priority varchar(255) not null,
    task_deadline timestamp ,
    is_done boolean,
    _created_at timestamp not null,
    _updated_at timestamp not null,
    primary key(task_id),
    foreign key (task_project) references projects(project_id),
    foreign key (task_user) references users(user_id)
);

create table time_entries(
    time_entrie_id int not null,
    time_entrie_user int not null,
    time_entrie_start timestamp not null,
    time_entrie_duration float not null,--time in seconds
    time_entrie_task int not null,
    _created_at timestamp not null,
    _updated_at timestamp not null,
    primary key(time_entrie_id),
    foreign key (time_entrie_user) references users(user_id),
    foreign key (time_entrie_task) references tasks(task_id)
);